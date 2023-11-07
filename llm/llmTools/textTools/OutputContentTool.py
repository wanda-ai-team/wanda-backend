
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
        
        if config.output == "twitter":
            output = Prompt.TWITTER_THREAD_PROMPT.value
        elif config.output == "instagram":
            output = Prompt.INSTAGRAM_POST_PROMPT.value
        elif config.output == "linkedin":
            output = Prompt.LINKEDIN_POST_PROMPT.value
        elif config.output == "blog":
            output = Prompt.BLOG_POST_PROMPT.value
        elif config.output == "newsletter":
            output = Prompt.NEWSLETTER_PROMPT.value
        elif config.output == "followupemail":
            output = Prompt.FOLLOWUP_EMAIL.value
            db = firestore.client()
            doc = db.collection("gongCalls")

            query = doc.where('callId', '==', config.gongCallId)
            docs = query.stream()
            for doc in docs:
                text = doc.get("transcript")
        elif config.output == "casestudy":
            output = Prompt.CASESTUDY_PROMPT.value
            db = firestore.client()
            doc = db.collection("gongCalls")

            query = doc.where('callId', '==', config.gongCallId)
            docs = query.stream()
            for doc in docs:
                text = doc.get("transcript")
        else:
            output = Prompt.TWITTER_THREAD_PROMPT.value
        
        PROMPT = PromptTemplate(template=output, input_variables=["text"])

        llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")

        
        chain = LLMChain(llm=llm, prompt=PROMPT, verbose=True)
        content = chain.run(text=text, return_only_outputs=True)

        return content