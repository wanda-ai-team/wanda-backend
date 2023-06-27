from collections import namedtuple
from llm.llmTools.LlmTools import LlmTools
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI

class SummarizationTool(LlmTools):
  def main(self, userText, config ):
    # text_splitter =  CharacterTextSplitter(chunk_size=3000)
    print(userText)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, chunk_overlap=0, separators=[" ", ",", "\n"]
    )

    texts = text_splitter.split_text(userText)

    documents = [Document(page_content=texts) for texts in texts]


    prompt_template = """You are a professional writter. I will give you a long text, and you will provide a summary of that text. Your summary should be informattive, factual, in-depth and correctly formatted, covering the most important aspects of the text, this summary will be used to create content for social media like twitter, instagram and others: 
     {text}
     SUMMARY: """
    
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(OpenAI(temperature=0), chain_type="map_reduce", map_prompt=PROMPT, combine_prompt=PROMPT)
    print("chain")
    content = chain({"input_documents": documents}, return_only_outputs=True)

    print("chain")
    print(content)
    return content.get('output_text')