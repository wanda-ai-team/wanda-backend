
from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from firebase_admin import firestore
import langchain
import openai
from openai import OpenAI
from pygame import mixer
import os
import io
import mimetypes
import requests
import ffmpeg
import youtube_dl
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY"),
)
class TranscribeYoutube(LlmTools):
        
    def main(self, userText, config):
        transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
        upload_endpoint = 'https://api.assemblyai.com/v2/upload'
        
        headers_auth_only = {'authorization': os.getenv("ASSEMBLYAI_API_KEY")}
        headers = {
            "authorization": os.getenv("ASSEMBLYAI_API_KEY"),
            "content-type": "application/json"
        }
        CHUNK_SIZE = 5242880
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg-location': './',
            'outtmpl': "./%(id)s.%(ext)s",
        }
        _id = config.videoId.strip() 
        print('Downloading', _id)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:       
            meta = ydl.extract_info(_id)
        save_location = meta['id'] + ".mp3"
        duration = meta['duration']
        print('Saved mp3 to', save_location)
        def read_file(filename):
            with open(filename, 'rb') as _file:
                while True:
                    data = _file.read(CHUNK_SIZE)
                    if not data:
                        break
                    yield data
        
        upload_response = requests.post(
            upload_endpoint,
            headers=headers_auth_only, data=read_file(save_location)
        )
        audio_url = upload_response.json()['upload_url']
        print('Uploaded to', audio_url)
        transcript_request = {
            'audio_url': audio_url
        }
        
        transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
        transcript_id = transcript_response.json()['id']
        polling_endpoint = transcript_endpoint + "/" + transcript_id
        print("Transcribing at", polling_endpoint)
        polling_response = requests.get(polling_endpoint, headers=headers)
        while polling_response.json()['status'] != 'completed':
            try:
                polling_response = requests.get(polling_endpoint, headers=headers)
            except:
                print("Expected wait time:", duration*2/5, "seconds")
                print("After wait time is up, call poll with id", transcript_id)
                return transcript_id
        _filename = transcript_id + '.txt'
        with open(_filename, 'w') as f:
            f.write(polling_response.json()['text'])
        print('Transcript saved to', _filename)