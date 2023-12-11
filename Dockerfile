FROM python:3.10
# 
WORKDIR /wanda-backend
# 
COPY ./requirements.txt /wanda-backend/requirements.txt
# 

# RUN export REGION=$(curl -s http://172.31.40.36/latest/dynamic/instance-identity/document | jq -r .region) && /root/.local/bin/aws ssm get-parameters --names PRODURL_SSM --region $REGION | grep Value | cut -d '"' -f4 >> /tmp/SSMParameter.txt && export DYNAMIC_SSM_VAR=$(cat /tmp/SSMParameter.txt) && npm run build
# RUN  /root/.local/bin/aws ssm get-parameters --names PRODURL_SSM --region $REGION | grep Value | cut -d '"' -f4 >> /tmp/SSMParameter.txt && export DYNAMIC_SSM_VAR=$(cat /tmp/SSMParameter.txt) && npm run build

RUN pip install  --use-deprecated=legacy-resolver --no-cache-dir --upgrade -r /wanda-backend/requirements.txt 

# 
COPY ./llm /wanda-backend/llm
COPY ./app /wanda-backend/app
COPY ./tools /wanda-backend/tools
COPY ./common /wanda-backend/common
COPY ./output /wanda-backend/output
COPY ./application.py /wanda-backend/application.py
COPY ./faiss_index /wanda-backend/faiss_index
#
CMD ["uvicorn", "application:application", "--host", "0.0.0.0", "--port", "8080"]