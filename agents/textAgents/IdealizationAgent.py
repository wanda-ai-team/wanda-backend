from collections import namedtuple
from agents.Agent import Agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

main_f = namedtuple('main', ())

class IdealizationAgent(Agent):
  def main(self):
    llm = ChatOpenAI(temperature=0.0)
    print("hello")
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