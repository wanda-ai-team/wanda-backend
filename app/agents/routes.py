import os
import openai
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
        llm = ChatOpenAI(temperature=0.0)
        math_llm = OpenAI(temperature=0.0)
        tools = load_tools(
            ["human", "llm-math"], 
            llm=math_llm,
        )

        agent_chain = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )

        answer = agent_chain.run("Give me 3 ideas to create a new twitter thread on the topics on")

        return answer
    else:
        return 'Content-Type not supported!'
