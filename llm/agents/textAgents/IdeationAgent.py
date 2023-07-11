from llm.ResponseModels import IdeationResponse
from llm.agents.Agent import Agent
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from llm.agents.textAgents.agentTools.AgentPrompt import Format, AgentPrompt, Prompt
from langchain.memory import ConversationBufferMemory
import json
from fastapi.encoders import jsonable_encoder

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
        json_result = json.loads(result)    
        
        ideas = []
        for i in range(len(json_result["list"])):
            ideas.append(json_result["list"][i]["item"])

        res = IdeationResponse(response=ideas)

        return jsonable_encoder(res)

