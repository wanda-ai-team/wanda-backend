import tempfile
import os
from collections import namedtuple
from llm.llmTools.LlmTools import LlmTools
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from langchain.chains import LLMChain
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from moviepy.editor import *

class YoutubeToTranscript(LlmTools):
    def main(self, config ):

        if "youtube.com" in config.url:
            url = config.url
            videoId = config.url.split("v=")[1]
        elif "youtu.be" in config.url:
            url = config.url
            videoId = config.url.split("/")[-1]

        try:
            transcript = YouTubeTranscriptApi.get_transcript(videoId)
            transcript = " ".join([t['text'] for t in transcript])
        except:
            transcript = youtubeDownload(url, videoId)

        return transcript
  
def youtubeDownload(url, videoId ):
    with tempfile.TemporaryDirectory() as temp_dir:
    
        # Download video audio
        yt = YouTube(url)


        # Get the first available audio stream and download this stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=temp_dir)

        # Convert the audio file to MP3
        audio_path = os.path.join(temp_dir, audio_stream.default_filename)
        audio_clip = AudioFileClip(audio_path)
        audio_clip.write_audiofile(os.path.join(temp_dir, f"{videoId}.mp3"))

        # Keep the path of the audio file
        audio_path = f"{temp_dir}/{videoId}.mp3"

        # Transscripe the MP3 audio to text
        transcript = transscribe_audio(audio_path)
        
        # Delete the original audio file
        os.remove(audio_path)
        
        return transcript.text

# Transcripe MP3 Audio function
def transscribe_audio(file_path):
    file_size = os.path.getsize(file_path)
    file_size_in_mb = file_size / (1024 * 1024)
    if file_size_in_mb < 25:
        with open(file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

        return transcript
    else:
        print("Please provide a smaller audio file (max 25mb).")