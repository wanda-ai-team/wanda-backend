# Backend

The backend API is a python flask project that is deployed in AWS

[https://github.com/wanda-ai-team/wanda-backend](https://github.com/wanda-ai-team/wanda-backend)

## How to execute

1. Clone the repository into your machine
2. Run the sh file on tools/run-env.sh
    1. sh tools/run-env.sh
3. Create an .env file with the
    
    ```
    OPENAI_API_KEY=
    GOOGLE_API_KEY=
    GOOGLE_CSE_ID=
    DB_USER=
    DB_PASS=
    DB_HOST=
    DB_PORT=
    DB_NAME=
    ```
    
4. Run the sh file on tools/run.sh
    1. sh tools/run.sh
5. Access your browser at
    1. [http://127.0.0.1:8000](http://127.0.0.1:5000/)

## How to deploy

1. Run the command pipenv requirements > requirements.txt
2. Commit and push the changes to the git repository
3. On your terminal run eb deploy

## Structure

This a backend API project.

It is built on top of FastAPI. [https://flask.palletsprojects.com/en/2.3.x/](https://fastapi.tiangolo.com/lo/)

PIPENV is used for python dependencies and environment

The structure is the following:

- [application.py](http://application.py) - It is the main application file, here it is defined the base of the application and the registration of blueprints
- app - main folder of the application
    
    ### Explanation
    
    - Endpoint folders always have the following structure
        - __init__.py where it creates the endpoint as a blueprint and imports the route file
        - [routes.py](http://routes.py) where the routes are defined with the logic that each does, if it’s more complex logic it should have its on file
        - other folder/files can exist to remove complex logic from the [routes.py](http://routes.py)
    - agents - main folder of the agents endpoint
    - llmTools - main folder of the tools endpoint
    - main - folder for anything that is mandatory and necessary
    - tests - folder for tests
    - tools - folder for generic tools that can be used across the project
    - auth - folder for everything that is auth wise, API_KEY
- common
    - tools - some common functions for across the project
- insomnia - latest json insomnia export
- llm
    - agents
        - textAgents - logic for all the agents based on text
    - llmTools
        - textTools - logic for all the text tools

## Infrastructure

![Untitled](Backend%20c9b7bc652d57488c9600dd134a3d58d9/Untitled.png)