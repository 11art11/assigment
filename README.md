# Assigment - Test Project
This project demonstrate:
* automated deployment of node.js application with docker compose
* automated tests using Python and pytest

## Getting started
* clone the repository

      git clone: https://github.com/11art11/assigment
* requirements:
  * [python version 3.9 or above](https://www.python.org/downloads/)
  * [docker engine](https://docs.docker.com/engine/install/)
* Install the dependencies:

      pip install -r requirements.txt
* Run tests:

        python -m pytest tests

## Project Structure
    assigment/
    ├── .circleci/
    │   ├── config.yml           # config to automate pipeline with circleCI
    ├── decorators/
    │   ├── decorators.py         # Decorators for other functions
    ├── docker_utils/
    │   ├── dockercompose.py      # perform docker compose actions
    │   ├── dockercomposelogs.py  # get docker compose logs
    ├── fixtures/
    │   ├── conftest.py           # setup/teardown fixture
    ├── helpers/                  # set of helpers
    │   ├── fileobserver.py       # live monitoring on files
    │   └── ...          
    ├── tests/                  
    │   ├── test_file_content.py  # set of test for content validation
    │   └── test_performance.py   # set of performance tests
    ├── requirements.txt
    ├── Dockerfile
    └── docker-compose.yml        # docker compose file to automate deployment

## Assumptions

* The written tests are black-box tests, focusing on the external behavior of the application.
* The only change made to the application is the modification of input data.
* No additional intermediary infrastructure has been added, implying that the tests interact directly with the application without any intermediate components or systems.