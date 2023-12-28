import os
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import json
from llm.llmTools.LlmTools import LlmTools
from langchain.tools import GoogleSerperRun
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
def find_object_by_name(name, object_list):
    for obj in object_list:
        if obj.name == name:
            return obj
    return None

def find_object_by_value(name, object_list):
    for obj in object_list:
        if obj['name'] == name:
            return obj
    return None

class AssistantCreationTool(LlmTools):

    def main(self, userText, config):
        # Opening JSON file
        my_assistants = client.beta.assistants.list(
            order="desc",
            limit=20,
        )
        assistant = find_object_by_name('Tommy', my_assistants.data)
        
        f = open('assistants/assistants.json')
        data = json.load(f)

        if assistant != None:
            print('There is no Tommy bot')
            for i in data:
                createdAssistant = OpenAIAssistantRunnable.create_assistant(
                    name=i['name'],
                    instructions=i['instructions'],
                    tools=[GoogleSerperRun(api_wrapper=GoogleSerperAPIWrapper(serper_api_key="ee162ff3349808ffdd95299026d41537a73633fe"))],
                    model=i['model'],
                    as_agent=True,      
                )

        else:
            return
            # asisit = OpenAIAssistantRunnable({assistant.id})
            assistantOld = find_object_by_value('Tommy', data)
            if assistantOld != None:
                print(assistant.tools)
                assistant.tools = assistant.tools.append(GoogleSearchAPIWrapper()) # type: ignore
                print(assistant.tools)
                client.beta.assistants.update(
                    assistant.id,
                    instructions=assistantOld['instructions'],
                    tools=JSON.stringify(assistant.tools),
                    model=assistantOld['model'],
                )

            # i['tools'] = i['tools'].append(DuckDuckGoSearchRun())
           
            # client.beta.assistants.update()
       
        return