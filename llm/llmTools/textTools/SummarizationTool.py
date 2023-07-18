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

class SummarizationTool(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)

        if (userText.startswith("http")):
            fileType = userText.split("_-_-")[1]
            fileURL = userText.split("_-_-")[0]
            print(fileType)
            if ("pdf" in fileType):
                response = requests.get(fileURL)
                my_raw_data = response.content
                # with BytesIO(my_raw_data) as data:
                #     read_pdf = PyPDF2.PdfReader(data)

                #     print(len(read_pdf.pages))
                #     message = ""
                #     for page in range(len(read_pdf.pages)):
                #         message = message + read_pdf.pages[page].extract_text()
            elif ("text" in fileType):
                message = ""
                for line in urllib.request.urlopen(fileURL):
                    message = message + line.decode('utf-8')
            elif ("document" in fileType):
                message = ""
                response = requests.get(fileURL)
                my_raw_data = response.content
                with BytesIO(my_raw_data) as data:
                    document = ZipFile(data)
                    content = document.read('word/document.xml')
                    word_obj = BeautifulSoup(content.decode('utf-8'))
                    text_document = word_obj.findAll('w:t')
                    for t in text_document:
                        message = message + t.text
        else:
            message = userText

        print(message)
        return message
        if (message == ""):
            return "No text found"

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=0, separators=[" ", ",", "\n"]
        )

        texts = text_splitter.split_text(message)

        documents = [Document(page_content=texts) for texts in texts]

        prompt_template = """You are a professional writter. I will give you a long text, and you will provide a summary of that text. Your summary should be informattive, factual, in-depth and correctly formatted, covering the most important aspects of the text, this summary will be used to create content for social media like twitter, instagram and others: 
     {text}
     SUMMARY: """

        PROMPT = PromptTemplate(template=prompt_template,
                                input_variables=["text"])
        chain = load_summarize_chain(OpenAI(
            temperature=0), chain_type="map_reduce", map_prompt=PROMPT, combine_prompt=PROMPT)
        print(documents)
        print("chain")
        content = chain({"input_documents": documents},
                        return_only_outputs=True)

        return content.get('output_text')
