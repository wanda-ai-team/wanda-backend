import os
import openai
from llm.RequestModels import LlmRequest
from llm.llmTools.textTools.SummarizationTool import SummarizationTool
from fastapi import APIRouter, Depends

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
