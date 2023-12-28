
from fastapi.responses import StreamingResponse
from llm.llmTools.LlmTools import LlmTools
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel
from langchain.schema import HumanMessage, SystemMessage

from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from firebase_admin import firestore
import langchain
import pinecone
import os
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import openai

class StreamChatTool(LlmTools):
    def main(self, userText, config):
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
            # next to api key in console
            environment=os.getenv("PINECONE_ENV"),
        )

        query = "You are a simple pdf and you are answering questions, get the information you have about simple pdf"
        chatMessages = []

        text_field = "text"

        embed = OpenAIEmbeddings()
        # switch back to normal index for langchain
        
        index_name = os.getenv("PINECONE_INDEX")	
        print(index_name)
        index = pinecone.Index(index_name)

        vectorstore = Pinecone(
            index, embed.embed_query, text_field
        )

        context = vectorstore.similarity_search(
            query,  # our search query
            k=3  # return 3 most relevant docs
        )

        finalContext = ""
        for i in context:
            finalContext = finalContext + i.page_content + " "

        for value in userText:
            
            if(value.get("role") == "user"):
                chatMessages.append(HumanMessage(content=value.get("content")))
            else:
                chatMessages.append(SystemMessage(content=value.get("content")))
        print(chatMessages)

        chain = ConversationChain(llm=ChatOpenAI(temperature=0, streaming=True, model="gpt-4-1106-preview"), verbose=True)
        return StreamingResponse.from_chain(chain, chatMessages, media_type="text/event-stream")
