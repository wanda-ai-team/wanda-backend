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
from langchain.chat_models import ChatOpenAI
import json
class SummarizationTool(LlmTools):
    def main(self, userText, config):
        message = userText

        print(message)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=0, separators=[" ", ",", "\n"]
        )

        texts = text_splitter.split_text(message)

        documents = [Document(page_content=texts) for texts in texts]

        print("documents")

        prompt_template = """
As a professional summarizer, create a concise and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:

Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness.

Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

Rely strictly on the provided text, without including external information.

Format the summary in paragraph form for easy understanding.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, concise, and reader-friendly manner.

Text: {text}"""

        PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(ChatOpenAI(temperature=0, model="gpt-4-1106-preview"), chain_type="map_reduce", map_prompt=PROMPT, combine_prompt=PROMPT)
        content = chain({"input_documents": documents}, return_only_outputs=True)
        print(content.get('output_text'))
        return content.get('output_text')