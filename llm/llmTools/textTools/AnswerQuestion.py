
from langchain.chains import LLMChain
from llm.llmTools.LlmTools import LlmTools
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

class AnswerQuestionTool(LlmTools):
    def main(self, userText, config):

        text = userText

        print("outputContentTool")
        print(userText)

        output = """ {text} """

        PROMPT = PromptTemplate(template=output, input_variables=["text"])

        llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview" )

        chain = LLMChain(llm=llm, prompt=PROMPT, verbose=True)
        print("1")
        content = chain.run(text=text, return_only_outputs=True, response_format={"type": "json_object"})
        print("content")
        print(content)
        print("2")

        return content