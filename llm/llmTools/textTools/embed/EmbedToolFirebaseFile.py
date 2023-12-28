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
import requests
import docx
from simplify_docx import simplify
import io
from langchain.document_loaders import Docx2txtLoader
import shutil
from langchain.text_splitter import RecursiveCharacterTextSplitter



class EmbedToolFirebaseFile(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        try:
            fileName = "tmp/sample.json"
            URL = "https://firebasestorage.googleapis.com/v0/b/wanda-dev-47016.appspot.com/o/knowledge%2Fsequences%2FAmple%20Sequences.docx?alt=media&token=e7a9a8da-604b-46c2-a3a8-ef3b674224a6"
            response = requests.get(URL, stream=True)

            with open(fileName, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            # coerce to JSON using the standard options
            loader  = Docx2txtLoader(fileName)
            data = loader.load()

            if os.path.exists(fileName):
                os.remove(fileName)
            
            fullText = data

            text_splitter = RecursiveCharacterTextSplitter(
                # Set a really small chunk size, just to show.
                chunk_size = 5000,
                chunk_overlap  = 20,
                length_function = len,
                add_start_index = True,
            )

            texts = text_splitter.split_documents(fullText)
            
            embeddings_model = OpenAIEmbeddings()

            pinecone.init(
                api_key=os.getenv("PINECONE_API_KEY"),
                environment=os.getenv("PINECONE_ENV"),
            )

            index_name = os.getenv("PINECONE_INDEX")

            if index_name not in pinecone.list_indexes():
                pinecone.create_index(
                    name=index_name,
                    metric='cosine',
                    dimension=1536
                )
            index = pinecone.Index(index_name)
            vectorstore = Pinecone(index, embeddings_model.embed_query, "text")
            vectorstore.add_documents(texts)
            
            return vectorstore

        except:

            raise HTTPException(status_code=500, detail="Item not found")
        
