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
from fastapi import  HTTPException


class EmbedTool(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        try:
            
            embeddings = OpenAIEmbeddings()
            text = userText

            pinecone.init(
                api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
                # next to api key in console
                environment=os.getenv("PINECONE_ENV"),
            )

            index_name = os.getenv("PINECONE_INDEX")

            # First, check if our index already exists. If it doesn't, we create it
            if index_name not in pinecone.list_indexes():
                # we create a new index
                pinecone.create_index(
                    name=index_name,
                    metric='cosine',
                    dimension=1536
                )

            index = pinecone.Index(index_name)
            # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
            print(config)
            vectorstore = Pinecone(index, embeddings.embed_query, "text")

            test = vectorstore.add_texts([text], [{'company': config.company, 'url': config.url, 'type of content': config.typeOfContent}])

            return test

        except:

            raise HTTPException(status_code=404, detail="Item not found")
        
