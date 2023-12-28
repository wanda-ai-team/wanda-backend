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
import time
from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup
import json
from bs4.element import Comment

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

def get_organic_results(query, num_results=3): 
    params = {
        "q": query,
        # "tbm": "nws",
        # "location": location,
        "num": str(num_results),
        "api_key": "c0b8a9033814b2e6ad203959c335599929b9d4dda6ee92ed4d6ba715df48a237"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    news_results = results.get("organic_results", [])
    urls = []
    for result in news_results:
        print(result['link'])
        urls.append(result['link'])

    return urls

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True



def scrape_website(url):
    headers = { 'User-Agent': 'Mozilla/5.0'} 
    response = requests.get(url, headers=headers)
    print(response.content)
    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup (page_content, 'html.parser') 
        # soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        formatted_data = u" ".join(t.strip() for t in visible_texts)
        # paragraphs = soup.find_all('p')
        # paragraphs.append(soup.find_all('h1'))
        # paragraphs.append(soup.find_all('h2'))
        # paragraphs.append(soup.find_all('h3'))
        # paragraphs.append(soup.find_all('h4'))
        # paragraphs.append(soup.find_all('h5'))
        # paragraphs.append(soup.find_all('h6'))
        # paragraphs.append(soup.find_all('span'))
        # paragraphs.append(soup.find_all('div'))
        
        # print(paragraphs)        
        # scraped_data = [p.get_text() for p in paragraphs] 
        # formatted_data = "\n".join(scraped_data)
        return url, formatted_data # Return both URL and content
    else:
        return url, "Failed to retrieve the webpage"
    

class AssistantCreationWithGoogleTool(LlmTools):

    def main(self, userText, config):
        # Opening JSON file
        # my_assistants = client.beta.assistants.list(
        #     order="desc",
        #     limit=20,
        # )
        # assistant = find_object_by_name('Tommy', my_assistants.data)
        
        
        assistant = client.beta.assistants.retrieve("asst_gY9QDqG5oX0yHbpIxSLjlJvk")
        
        f = open('assistants/assistants.json')
        data = json.load(f)

        if assistant == None:
            print('There is no Tommy bot')
            print("data")
            print(data)
            for i in data:
                print(i)
                createdAssistant = OpenAIAssistantRunnable.create_assistant(
                    name=i['name'],
                    instructions=i['instructions'],
                    tools=[{
                        "type": "function",
                        "function": {
                        "name": "get_organic_results",
                        "description": "Fetch news URLS based on a search query",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                },
                                "query": {"type": "string", "description": "Search query"},
                                "num_results": {"type": "integer", "description": "Number of results to return"}, 
                                "location": {"type": "string", "description": "Location for search context"},
                                "required":["query"],
                            }
                        }
                    }, {
                        "type": "function",
                        "function": {
                        "name": "scrape_website",
                        "description": "Scrape the textual content from a given URL",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "url": {"type": "string", "description": "URL to scrape"},
                                },
                                "required":["url"],
                            }
                        }
                    }, {'type': "retrieval"}
                    ],
                    model=i['model'],
                    as_agent=True,      
                )

                print("createdAssistant")
                print(createdAssistant)

        else:
            # asisit = OpenAIAssistantRunnable({assistant.id})
            assistantOld = find_object_by_value('Tommy', data)
            thread = client.beta.threads.create()

            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                content=userText,
                role="user"
            )
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id,
            )
            i = 0
            while(run.status not in ["completed", "failed", "requires_action"]):
                if(i > 0):
                    time.sleep(10)
                
                run = client.beta.threads.runs.retrieve(     
                    thread_id=thread.id,
                    run_id=run.id
                )
                i+=1
                print(run.status)
            

            i = 0
            while(run.status not in ["completed", "failed"]):
                if(i > 0):
                    time.sleep(10)
                
                run = client.beta.threads.runs.retrieve(     
                    thread_id=thread.id,
                    run_id=run.id
                )
                i+=1

                if run.status == "requires_action" and run.required_action != None:
                    tools_to_call = run.required_action.submit_tool_outputs.tool_calls
                    tool_output_array = []
                    print("Tools to call")
                    print(tools_to_call)
                    for tool in tools_to_call:
                        tool_call_id = tool.id
                        tool_call_name = tool.function.name
                        tool_call_arg = tool.function.arguments
                        content = ""
                        if tool_call_name == "get_organic_results":
                            new_urls = get_organic_results(userText)
                            if new_urls:
                                url, content = scrape_website(new_urls[0])
                            
                            print(content)
                            tool_output_array.append({
                                "tool_call_id": tool_call_id,
                                "output": content
                            })

                        if tool_call_name == "scrape_website":
                            print(url)
                            url, content = scrape_website(url)

                            tool_output_array.append({
                                "tool_call_id": tool_call_id,
                                "output": content
                            })

                        run = client.beta.threads.runs.submit_tool_outputs(
                            thread_id=thread.id,
                            run_id=run.id,
                            tool_outputs=tool_output_array
                        )

                print(run.status)

            if run.status == "completed":
                messages = client.beta.threads.messages.list(
                    thread_id=thread.id
                )
                for each in messages:
                    return each.content[0].text.value # type: ignore

            # if assistantOld != None:
            #     print(assistant.tools)
            #     assistant.tools = assistant.tools.append(GoogleSearchAPIWrapper()) # type: ignore
            #     print(assistant.tools)
            #     client.beta.assistants.update(
            #         assistant.id,
            #         instructions=assistantOld['instructions'],
            #         tools=JSON.stringify(assistant.tools),
            #         model=assistantOld['model'],
            #     )

            # i['tools'] = i['tools'].append(DuckDuckGoSearchRun())
           
            # client.beta.assistants.update()
       
        return