import os
from llm.RequestModels import LlmRequest
from llm.llmTools.textTools.AnswerQuestion import AnswerQuestionTool
from llm.llmTools.textTools.EmbedTool import EmbedTool
from llm.llmTools.textTools.GetEmbeddedContent import GetEmbeddedContent
from llm.llmTools.textTools.OutputContentTool import OutputContentTool
from llm.llmTools.textTools.TranscribeYoutube import TranscribeYoutube
from llm.llmTools.textTools.VectorDBQueryTool import VectorDBQueryTool
from llm.llmTools.textTools.SummarizationTool import SummarizationTool
from fastapi import APIRouter, Depends

from llm.llmTools.textTools.TextToSocialMediaTool import TextToSocialMediaTool
from llm.llmTools.videoTools.YoutubeToTranscript import YoutubeToTranscript

llmToolsRouter = APIRouter()


@llmToolsRouter.get("/test")
def test():
    return 'answer'

@llmToolsRouter.post("/summarize")
def summarize(llmRequest: LlmRequest = None):  # type: ignore
    tool = SummarizationTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/textToPost")
def textToPost(llmRequest: LlmRequest = None):  # type: ignore
    tool = TextToSocialMediaTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/youtubeToTranscript")
def youtubeToTranscript(llmRequest: LlmRequest = None):  # type: ignore
    tool = YoutubeToTranscript()
    answer = tool.main(llmRequest.config)
    return answer

@llmToolsRouter.post("/embedText")
def embedText(llmRequest: LlmRequest = None): # type: ignore
    tool = EmbedTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/vectorDBQuery")
def vectorDBQueryTool(llmRequest: LlmRequest = None): # type: ignore
    tool = VectorDBQueryTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/getEmbeddedContent")
def getEmbeddedContent(llmRequest: LlmRequest = None): # type: ignore
    tool = GetEmbeddedContent()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/outputContent")
def getOutputContent(llmRequest: LlmRequest = None): # type: ignore
    tool = OutputContentTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer


@llmToolsRouter.post("/transcribeYoutube")
def getOutputContent(llmRequest: LlmRequest = None): # type: ignore
    tool = TranscribeYoutube()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer

@llmToolsRouter.post("/answerQuestionTool")
def getOutputContent(llmRequest: LlmRequest = None): # type: ignore
    tool = AnswerQuestionTool()
    answer = tool.main(llmRequest.userPrompt, llmRequest.config)
    return answer






