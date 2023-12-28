import os
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import json
from llm.llmTools.LlmTools import LlmTools
from langchain.tools import GoogleSerperRun
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from slack_sdk import WebClient
import assemblyai as aai
import urllib.request
import requests


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Transcript(LlmTools):

    def main(self, userText, config):
        try:

            slack_token = os.environ["SLACK_TOKEN"]
            client = WebClient(token=slack_token)
            
            message1 = client.chat_postMessage(channel=config.slackChannel, text="Getting file ...", thread_ts=config.slackThreadTs)
            response = requests.get(config.audioUrl, headers={"Authorization": "Bearer " + slack_token})
            headers = {
                'Authorization': 'Bearer ' + slack_token
            }
            filename = 'output_file.mp4'  # Replace with your desired file name and extension
            response = requests.get(config.audioUrl, headers=headers, stream=True)

                
            if response.status_code == 200:
                if "video/mp4" in response.headers.get("Content-Type", ""):
                    with open(filename, 'wb') as file:
                        file.write(response.content)
                    print(f"File downloaded successfully: {filename}")
                    
                    client.chat_postMessage(channel=config.slackChannel, text="Transcribing file ...", thread_ts=config.slackThreadTs)

                    configAAI = aai.TranscriptionConfig(
                        summarization=True,
                        summary_model=aai.SummarizationModel.informative,
                        summary_type=aai.SummarizationType.bullets
                    )

                    transcript = aai.Transcriber().transcribe(filename, configAAI)

                    if transcript != None and transcript.summary != None:
                        slackMessage = "Summary: \n\n"
                        slackMessageF = slackMessage + transcript.summary
                        client.chat_postMessage(channel=config.slackChannel, text=slackMessageF, thread_ts=config.slackThreadTs)
                    else:
                        client.chat_postMessage(channel=config.slackChannel, text="No summary available", thread_ts=config.slackThreadTs)
                else:
                    print(response.headers.get("Content-Type", ""))
            else:
                print(f"Failed to download file: {response.status_code}")
            return 

        except Exception as error:
            # handle the exception
            print("An exception occurred:", error) # An exception occurred: division by zero



        # Opening JSON file
        # config = aai.TranscriptionConfig(punctuate=False, format_text=False)

        # transcriber = aai.Transcriber(config=config)

        # # will use the same config for all `.transcribe*(...)` operations
        # transcriber.transcribe("https://example.org/audio.wav")
       
        return