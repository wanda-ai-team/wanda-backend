FROM python:3.10
# 
WORKDIR /wanda-baclend
# 
COPY ./requirements.txt /wanda-baclend/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /wanda-baclend/requirements.txt 
# 
COPY ./agents /code/agents
COPY ./app /code/app
COPY ./tools /code/tools
COPY ./application.py /code/application.py
#
CMD ["uvicorn", "application:application", "--host", "0.0.0.0"]