from collections import namedtuple
from llm.llmTools.LlmTools import LlmTools
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
import requests
from bs4 import BeautifulSoup
import urllib.request  # the lib that handles the url stuff
import requests
# import PyPDF2
from io import BytesIO
from zipfile import ZipFile
from langchain.embeddings import OpenAIEmbeddings
import pinecone
import os
from langchain.vectorstores import Pinecone
from langchain.chains.question_answering import load_qa_chain
from fastapi import  HTTPException


class GetEmbeddedContent(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        try:
            embeddings = OpenAIEmbeddings()
            query = userText

            pinecone.init(
                api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
                # next to api key in console
                environment=os.getenv("PINECONE_ENV"),
            )
            index_name = os.getenv("PINECONE_INDEX")
            score = False

            print("olaaa")

            docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
            # index = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings, text_key="joao.airesmatos@gmail.com-website")

            if score:
                similar_docs = docsearch.similarity_search_with_score(query, k=2)
            else:
                similar_docs = docsearch.similarity_search(query, k=2)

            print(similar_docs)
            return  similar_docs

        except:
            raise HTTPException(status_code=404, detail="Item not found")
