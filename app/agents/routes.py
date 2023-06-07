import os
import openai
from agents.textAgents.IdealizationAgent import IdealizationAgent
from app.agents import bp
from flask import request
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

openai.api_key = os.getenv("OPENAI_API_KEY")


@bp.route("/<place>")
def place(place="Berlin"):
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=['place'],
        template="What are the 3 best places to eat in {place}?",
    )
    question = prompt.format(place=place)
    answer =  llm(question).split("\n\n")
    print(answer)
    return answer

@bp.route("/ideas", methods=['POST'])
def ideas():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        agent = IdealizationAgent("IdealizationAgent")
        answer = agent.main()
        return answer
    else:
        return 'Content-Type not supported!'
