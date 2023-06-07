# Backend

The backend API is a python flask project that is deployed in AWS

[https://github.com/wanda-ai-team/wanda-backend](https://github.com/wanda-ai-team/wanda-backend)

## How to execute

1. Clone the repository into your machine
2. Run the sh file on tools/run-env.sh
    1. sh tools/run-env.sh
3. Create an .env file with the OPENAI_API_KEY
4. Run the sh file on tools/run.sh
    1. sh tools/run.sh
5. Access your browser at
    1. [http://127.0.0.1:5000](http://127.0.0.1:5000/)

## How to deploy

1. Commit and push the changes to the git repository
2. On your terminal run eb deploy

## Structure

This a backend API project.

It is built on top of Flask. [https://flask.palletsprojects.com/en/2.3.x/](https://flask.palletsprojects.com/en/2.3.x/)

It uses the blueprint concept for the structure of the endpoints

Pipenv is used for pythong dependencies and environment

The structure is the following:

- [application.py](http://application.py) - It is the main application file, here it is defined the base of the application and the registration of blueprints
- app - main folder of the application
    
    ### Explanation
    
    - Endpoint folders always have the following structure
        - __init__.py where it creates the endpoint as a blueprint and imports the route file
        - [routes.py](http://routes.py) where the routes are defined with the logic that each does, if it’s more complex logic it should have its on file
        - other folder/files can exist to remove complex logic from the [routes.py](http://routes.py)
    - agents - main folder of the agents endpoint
        - here the main logic for all agents should be created
    - main - folder for anything that is mandatory and necessary
    - tests - folder for tests
    - tools - folder for generic tools that can be used across the project

## Infrastructure

![Untitled](Backend%20c9b7bc652d57488c9600dd134a3d58d9/Untitled.png)