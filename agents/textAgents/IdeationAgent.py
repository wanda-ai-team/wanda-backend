from collections import namedtuple
from agents.Agent import Agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

main_f = namedtuple('main', ())

class IdeationAgent(Agent):
  def main(self, userPrompt, systemPrompt, config ):
    # llm = ChatOpenAI(temperature=0.0)
    # tools = load_tools(
    #     ["human"], 
    #     llm=llm,
    # )

    # agent_chain = initialize_agent(
    #     tools,
    #     llm,
    #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    # )
    search = GoogleSearchAPIWrapper()

    tool = Tool(
        name = "Google Search",
        description="Search Google for recent results.",
        func=search.run
    )
    answer = tool.run("Give me 3 ideas to create a new twitter thread on the following topic: " + userPrompt)

    return answer