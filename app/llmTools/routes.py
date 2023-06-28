import os
import openai
from llm.RequestModels import LlmRequest
from llm.llmTools.textTools.SummarizationTool import SummarizationTool
from fastapi import APIRouter, Depends

from llm.llmTools.textTools.TextToSocialMediaTool import TextToSocialMediaTool
from llm.llmTools.videoTools.YoutubeToTranscript import YoutubeToTranscript

llmToolsRouter = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")

@llmToolsRouter.get("/test")
def test():
    return 'answer'

@llmToolsRouter.post("/summarize")
def summarize(llmRequest: LlmRequest):
    tool = SummarizationTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/textToPost")
def summarize(llmRequest: LlmRequest):
    tool = TextToSocialMediaTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/youtubeToTranscript")
def youtubeToTranscript(llmRequest: LlmRequest):
    tool = YoutubeToTranscript()
    answer = tool.main(llmRequest.config)
    return answer