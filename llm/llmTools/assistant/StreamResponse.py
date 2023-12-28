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
from fastapi import FastAPI, HTTPException
from starlette.responses import StreamingResponse
import openai
import async_timeout
import asyncio

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

GENERATION_TIMEOUT_SEC = 60

async def stream_generator(subscription):
    async with async_timeout.timeout(GENERATION_TIMEOUT_SEC):
        try:
            async for chunk in subscription:
                yield post_processing(chunk)
        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Stream timed out")
class StreamResponseTool(LlmTools):

    async def main(self, userText, config):
        # Opening JSON file
        try:    
            stream = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": "Say this is a test"}],
                stream=True,
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
        except openai.OpenAIError:
            raise HTTPException(status_code=500, detail='OpenAI call failed')
       
        return