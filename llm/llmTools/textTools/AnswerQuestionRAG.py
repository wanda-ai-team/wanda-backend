
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
        embed_model = OpenAIEmbeddings()

        new_db = FAISS.load_local("faiss_index", embed_model)

        retriever = new_db.as_retriever()

        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)

        model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview" )

        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser()
        )

        content = chain.invoke(userText)


        return content