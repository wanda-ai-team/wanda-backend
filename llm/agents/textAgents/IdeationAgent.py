from common.tools.ReadFile import readFile
from llm.agents.Agent import Agent
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from llm.agents.textAgents.agentTools.FixedWriteFileTool import FixedWriteFileTool
from llm.agents.textAgents.agentTools.AgentPrompt import Format, AgentPrompt, Prompt
from langchain.memory import ConversationBufferMemory
import json
from langchain.utilities import SerpAPIWrapper

from llm.agents.textAgents.agentTools.OutputFormatter import OutputFormatter


class IdeationAgent(Agent):
    def main(self, userPrompt, systemPrompt, config):
        llm = ChatOpenAI(temperature=0)
        tools = load_tools(["ddg-search", "serpapi"], llm=llm)
        tools.append(OutputFormatter())
        # tools.append(FixedWriteFileTool(root_dir="./output/"))

        memory = ConversationBufferMemory()

        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                 verbose=True, memory=memory, handle_parsing_errors=True)

        prompt_template = AgentPrompt()

        prompt = prompt_template.PassInPromptInput(
            userPrompt, Format.LIST, Prompt.IDEATIONPROMPT)

        result = agent.run(prompt)

        return json.loads(result)

