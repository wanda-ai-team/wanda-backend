
from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from firebase_admin import firestore
import langchain
import openai

class OutputContentTool(LlmTools):
    def main(self, userText, config):

        text = userText

        print("outputContentTool")
        print(config)

        if config.output == None:
            output = Prompt.SUMMARY_PROMPT.value
        elif "twitter" in config.output.lower():
            output = Prompt.TWITTER_THREAD_PROMPT.value
        elif "instagram" in config.output.lower():
            output = Prompt.INSTAGRAM_POST_PROMPT.value
        elif "linkedin" in config.output.lower():
            output = Prompt.LINKEDIN_POST_PROMPT.value
        elif "blog" in config.output.lower():
            output = Prompt.BLOG_POST_PROMPT.value
        elif "landing" in config.output.lower():
            output = Prompt.LANDING_COPY_PROMPT.value
        elif "scrape" in config.output.lower():
            output = Prompt.SCRAPING_PROMPT.value
        elif "summary" in config.output.lower():
            output = Prompt.SUMMARY_PROMPT.value
        elif "email" in config.output.lower():
            output = Prompt.FOLLOWUP_EMAIL.value
        elif "study" in config.output.lower():
            output = Prompt.CASESTUDY_PROMPT.value
        else:
            output = Prompt.TWITTER_THREAD_PROMPT.value
            
        if config.gongCallId and config.gongCallId != "":
            db = firestore.client()
            doc = db.collection("gongCalls")

            query = doc.where('callId', '==', config.gongCallId)
            docs = query.stream()
            for doc in docs:
                text = doc.get("transcript")    

        PROMPT = PromptTemplate(template=output, input_variables=["text"])

        llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview" )

        chain = LLMChain(llm=llm, prompt=PROMPT, verbose=True)
        content = chain.run(text=text, return_only_outputs=True, response_format={"type": "json_object"})

        return content