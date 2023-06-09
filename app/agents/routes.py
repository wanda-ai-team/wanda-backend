import os
import openai
from agents.textAgents.IdeationAgent import IdeationAgent
from flask import request
from application import application
from fastapi import FastAPI
from pydantic import BaseModel

openai.api_key = os.getenv("OPENAI_API_KEY")

class AgentRequest(BaseModel):
    userPrompt: str
    systemPrompt: str | None = None
    config: str


@application.get("/agents/ideasT")
def ideasT():
    agent = IdeationAgent("IdeationAgent")
    answer = agent.main("ai", "ai", "ai")
    return answer
    
@application.post("/agents/ideas")
def ideas(agentRequest: AgentRequest):
    agentRequest_dict = agentRequest.dict()
    print(agentRequest_dict)
    agent = IdeationAgent("IdeationAgent")
    answer = agent.main(agentRequest.userPrompt, agentRequest.systemPrompt, agentRequest.config)
    return answer



# @bp.route("/<place>")
# def place(place="Berlin"):
#     llm = OpenAI(temperature=0.9)
#     prompt = PromptTemplate(
#         input_variables=['place'],
#         template="What are the 3 best places to eat in {place}?",
#     )
#     question = prompt.format(place=place)
#     answer =  llm(question).split("\n\n")
#     print(answer)
#     return answer


