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
      output = Prompt.TWITTER_THREAD_PROMPT
    elif config.output == "instagram":
      output = Prompt.INSTAGRAM_POST_PROMPT
    elif config.output == "linkedin":
      output = Prompt.LINKEDIN_POST_PROMPT
    elif config.output == "blog":
      output = Prompt.BLOG_POST_PROMPT
    else: 
      output = Prompt.TWITTER_THREAD_PROMPT

    llm = OpenAI(temperature=0.9)
    
    prompt = PromptTemplate(
        input_variables=["tone", "writing"],
        template=output.value
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    content = chain.run(tone=config.tone, writing=config.writing)

    return content