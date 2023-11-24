
from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from llm.llmTools.textTools.tools.ToolsPrompt import Prompt
from firebase_admin import firestore
import langchain
import openai

class AnswerQuestionTool(LlmTools):
    def main(self, userText, config):

        text = userText

        output = Prompt.ANSWER_QUESTION_PROMPT.value

        PROMPT = PromptTemplate(template=output, input_variables=["text"])

        llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview" )

        chain = LLMChain(llm=llm, prompt=PROMPT, verbose=True)
        content = chain.run(text=text, return_only_outputs=True, response_format={"type": "json_object"})

        return content