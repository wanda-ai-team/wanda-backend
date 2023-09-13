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

class VectorDBQueryTool(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        print(type(userText))
        print(type(config.index))
        embeddings = OpenAIEmbeddings()
        query = userText

        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
            environment=os.getenv("PINECONE_ENV"),  # next to api key in console
        )

        index_name = config.index + "-index"

        docsearch = Pinecone.from_existing_index(index_name, embeddings)

        docs = docsearch.similarity_search(query)
        
        print(docs[0].page_content)

        return docs[0].page_content