
from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from firebase_admin import firestore
import langchain
import openai
from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS
from zipfile import ZipFile
from langchain.embeddings import OpenAIEmbeddings
import pinecone
import os
from langchain.vectorstores import Pinecone
from fastapi import  HTTPException
from tqdm.auto import tqdm  # for progress bar

from langchain.text_splitter import RecursiveCharacterTextSplitter

class AnswerQuestionRAGTool(LlmTools):
    def main(self, userText, config): 
        try:
            try:
                print("entered")
                # new_db = FAISS.load_local("/wanda-backend/faiss_index", embed_model)
                embeddings = OpenAIEmbeddings()
                index_name = os.getenv("PINECONE_INDEX")

                pinecone.init(
                    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
                    # next to api key in console
                    environment=os.getenv("PINECONE_ENV"),
                )
                vectordb = Pinecone.from_existing_index(
                    index_name=index_name,
                    embedding=embeddings,
                )
                retriever = vectordb.as_retriever()
            
            except Exception as error:
                # handle the exception
                print("An exception occurred:", error) # An exception occurred: division by zero
                retriever = ""

            print("retrieved")

            template = """Answer the question based only on the following context:
            {context}

            Question: {question}
            """

            print("template")
            print(template)
            print(userText)
            prompt = ChatPromptTemplate.from_template(template)

            model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview" )
            print("ola")
            print(retriever)
            chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | model
                | StrOutputParser()
            )

            content = chain.invoke(userText)


            return content
        except Exception as error:
            # handle the exception
            print("An exception occurred:", error) # An exception occurred: division by zero
            raise HTTPException(status_code=500, detail="Backend error")