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
from tqdm.auto import tqdm  # for progress bar

from langchain.text_splitter import RecursiveCharacterTextSplitter


class EmbedVectorDBTool(LlmTools):
    def main(self, userText, config):
        print("o")
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        try:
            
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

            # index = pinecone.Index(index_name)
            # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`

            embed_model = OpenAIEmbeddings()

            # res = embed_model.embed_query(text)

            
            print(text)
            batch_size = 100

            text_splitter = RecursiveCharacterTextSplitter(
                # Set a really small chunk size, just to show.
                chunk_size = 2000,
                chunk_overlap  = 0,
                length_function = len,
            )
            # Split the file content 

            book_texts = text_splitter.create_documents([text])

            for i in range(0, len(book_texts)):
                book_texts[i].metadata["title"] = config.inputDocTitle

            docsearch = Pinecone.from_documents(book_texts, embed_model, index_name = index_name)

            print("Indexing documents...")
            print(docsearch)

            return "success"

        except Exception as error:
            # handle the exception
            print("An exception occurred:", error) # An exception occurred: division by zero
            raise HTTPException(status_code=404, detail="Item not found")
        
