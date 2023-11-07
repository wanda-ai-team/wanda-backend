from llm.agents.textAgents.agentTools.AgentOutputModels import ItemList, Item, Summary
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from enum import Enum


class Format(Enum):
    SUMMARY = "Summary"
    LIST = "List"


class Prompt(Enum):
    REASEARCHPROMPT = """  You are a research agent.
As a research agent, your task is to use the provided tools of duckduckgo_search and Wikipedia to research on the given topic.
Your goal is to collect detailed and accurate information on the topic, utilizing both tools to gather a wide range of sources. 
Once you have completed your research, you must create an original, impersonal summary of your findings in the format specified as the final answer.
Please note that your summary should be well-organized and structured in a way that effectively communicates the main points of your research. 
You should focus on providing a concise and clear summary of the information you have found, without including any personal opinions or biases.
Furthermore, you should use additional online resources as necessary to supplement your findings from duckduckgo_search and Wikipedia. 
Your research should be thorough and comprehensive, taking into account relevant historical, cultural, scientific, or other contextual information related to the topic.
You are not done until you have created an ORIGINAL, IMPERSONAL summary of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.

{format}
    
Topic: {request}
And remember to create an ORIGINAL, IMPERSONAL summary of the results of this research IN THE FORMAT SPECIFIED AS THE FINAL ANSWER!"""

    IDEATIONPROMPT = """ 
You are an ideation agent with a mission to harness the power of social media marketing.
Your arsenal includes the serapi tool, which is your key to uncovering the freshest and most pertinent Twitter topics.
Your ultimate goal is to craft a collection of captivating Twitter thread ideas that seamlessly blend the current trending themes on Twitter with the objectives of the given business, allowing them to foster deeper connections with their audience: {request}
Your list should include at least five ideas for different types of posts, such as informational posts, opinion pieces, visual content, and interactive content. 
Your ideas should be engaging, thought-provoking, and shareable, with a focus on educating and entertaining the audience.
Additionally, please provide clear and concise descriptions of your ideas, including any relevant hashtags or calls to action that should be included in the posts.
When you have finished collecting your findings via duckduckgo_search and serapi tools, create an ORIGINAL, IMPERSONAL list of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.
You are not done until you outputted your findings using the format specified.

Output with the following format:
{format}
And remember to output the results of this ideation with the correct format!"""


class AgentPrompt:
    def PassInPromptInput(self, request: str, format: Format, prompt: Prompt) -> str:
        format_instructions = self.createFormatInstructions(format)
        
        prompt_template = PromptTemplate(template=prompt.value, input_variables=["request"], partial_variables={"format": format_instructions})
        
        return prompt_template.format(request=request)

    def createFormatInstructions(self, format):
        format_instructions = ''

        if(format == Format.LIST):
            format_instructions = PydanticOutputParser(pydantic_object=ItemList).get_format_instructions()
            itemListExample = self.create_list_example()
            
            example = """
An example of this would be the following:
"""+itemListExample.json()

            format_instructions = format_instructions+example

        else:
            format_instructions = PydanticOutputParser(pydantic_object=Summary).get_format_instructions()
            summaryExample = self.create_summary_example()
            example = """
An example of this would be the following:
"""+summaryExample.json()

            format_instructions = format_instructions+example

        return format_instructions

    def create_list_example(self):
        item1 = Item(item="Chicken Eggs",
            description="Eggs that come from chickens")
        item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
        item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

        itemListExample = ItemList(file_path="eggs.txt",
                        list=[item1, item2, item3])
                    
        return itemListExample

    def create_summary_example(self):
        summary = "Eggs are laid by animals and come from birds, reptiles, fish, amphibians, and even some mamals. They are also consumed in a variey of dishes."

        summaryExample = Summary(file_path="eggs.txt", summary=summary)

        return summaryExample