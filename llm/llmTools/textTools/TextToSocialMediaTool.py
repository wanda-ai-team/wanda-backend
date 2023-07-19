from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from langchain.chains import LLMChain


class TextToSocialMediaTool(LlmTools):
    def main(self, userText, config):
        # text_splitter =  CharacterTextSplitter(chunk_size=3000)
        if config.output == "twitter":
            output = Prompt.TWITTER_THREAD_PROMPT
        elif config.output == "instagram":
            output = Prompt.INSTAGRAM_POST_PROMPT
        elif config.output == "linkedin":
            output = Prompt.LINKEDIN_POST_PROMPT
        elif config.output == "blog":
            output = Prompt.BLOG_POST_PROMPT
        elif config.output == "newsletter":
            output = Prompt.NEWSLETTER_PROMPT
        else:
            output = Prompt.TWITTER_THREAD_PROMPT

        llm = OpenAI(temperature=0.9)

        prompt = PromptTemplate(
            input_variables=["tone", "writing", "text"],
            template=output.value
        )

        chain = LLMChain(llm=llm, prompt=prompt)

        if (config.tone == None or config.tone == ""):
            config.tone = "casual"
        if (config.writing == None or config.writing == ""):
            config.writing = "casual"

        content = chain.run(
            tone=config.tone,
            writing=config.writing,
            text=userText
        )

        return content
