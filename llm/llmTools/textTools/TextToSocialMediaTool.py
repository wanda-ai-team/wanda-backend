from collections import namedtuple
from llm.llmTools.LlmTools import LlmTools
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from langchain.chains import LLMChain

class TextToSocialMediaTool(LlmTools):
  def main(self, userText, config ):
    # text_splitter =  CharacterTextSplitter(chunk_size=3000)
    if config.output == "twitter":
      output = Prompt.TWITTERTHREADPROMPT
    elif config.output == "instagram":
      output = Prompt.TWITTERTHREADPROMPT
    else: 
      output = Prompt.TWITTERTHREADPROMPT

    llm = OpenAI(temperature=0.9)
    
    prompt = PromptTemplate(
        input_variables=["tone", "writing"],
        template=output.value
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    content = chain.run(tone=config.tone, writing=config.writing)

    return content