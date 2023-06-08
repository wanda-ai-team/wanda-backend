import os
import openai
from agents.textAgents.IdeationAgent import IdeationAgent
from app.agents import bp
from flask import request

openai.api_key = os.getenv("OPENAI_API_KEY")


# @bp.route("/<place>")
# def place(place="Berlin"):
#     llm = OpenAI(temperature=0.9)
#     prompt = PromptTemplate(
#         input_variables=['place'],
#         template="What are the 3 best places to eat in {place}?",
#     )
#     question = prompt.format(place=place)
#     answer =  llm(question).split("\n\n")
#     print(answer)
#     return answer

@bp.route("/ideasT")
def ideasT():
    agent = IdeationAgent("IdeationAgent")
    answer = agent.main()
    return answer
    
@bp.route("/ideas", methods=['POST'])
def ideas():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        request_data = request.get_json()
        if("userPrompt" not in request_data or "systemPrompt" not in request_data or "config" not in request_data):
            return "There are missing parameters from the request!"
        
        if(not str(request_data['userPrompt']) or not str(request_data['systemPrompt'])):
            return "userPrompt and systemPrompt must be strings!"

        userPrompt = request_data['userPrompt']
        systemPrompt = request_data['systemPrompt']
        config = request_data['config']

        agent = IdeationAgent("IdeationAgent")
        answer = agent.main(userPrompt, systemPrompt, config)
        return answer
    else:
        return 'Content-Type not supported!'
