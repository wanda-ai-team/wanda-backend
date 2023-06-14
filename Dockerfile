FROM python:3.10
# 
WORKDIR /wanda-backend
# 
COPY ./requirements.txt /wanda-backend/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /wanda-backend/requirements.txt 
# 
COPY ./agents /wanda-backend/agents
COPY ./app /wanda-backend/app
COPY ./tools /wanda-backend/tools
COPY ./application.py /wanda-backend/application.py
#
CMD ["uvicorn", "application:application", "--host", "0.0.0.0"]