import os
from llm.RequestModels import AgentRequest
from llm.agents.textAgents.IdeationAgent import IdeationAgent
from llm.agents.textAgents.ResearchAgent import ResearchAgent
from fastapi import APIRouter

agentsRouter = APIRouter()




@agentsRouter.get("/test")
def test():
    return 'answer'
    
@agentsRouter.post("/ideas")
def ideas(agentRequest: AgentRequest):
    agent = IdeationAgent()
    answer = agent.main(agentRequest.userPrompt, agentRequest.systemPrompt, agentRequest.config)
    return answer
    
@agentsRouter.post("/research")
def research(agentRequest: AgentRequest):
    agent = ResearchAgent()
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


