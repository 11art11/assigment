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
## Behaviour
* Downloads and extracts the application under test.
* Creates a set of input data for the test.
* Deploys the application on Docker using Docker Compose.
* Executes the tests on the deployed application.
* Archives the test artifacts for future reference or analysis.
* Removes the Docker containers after the tests are completed.

The purpose of this setup is to ensure a controlled environment for testing the application. By downloading and deploying the application, creating specific input data, and running the tests in a containerized environment, the setup helps ensure consistency and reproducibility of the test results. The archiving of test artifacts allows for further investigation and analysis if needed. Finally, the cleanup of Docker containers helps maintain the test environment clean and ready for subsequent tests.

## Project Structure
    assigment/
    ├── .circleci/
    │   ├── config.yml           # config to automate pipeline with circleCI
    ├── decorators/
    │   ├── decorators.py         # Decorators for other functions
    ├── docker_utils/
    │   ├── dockercompose.py      # perform docker compose actions
    │   ├── dockercomposelogs.py  # get docker compose logs
    ├── helpers/                  # set of helpers
    │   ├── fileobserver.py       # live monitoring on files
    │   └── ...          
    ├── tests/                  
    │   ├── conftest.py           # setup/teardown fixture
    │   ├── test_file_content.py  # set of test for content validation
    │   └── test_performance.py   # set of performance tests
    ├── requirements.txt
    ├── Dockerfile
    └── docker-compose.yml        # docker compose file to automate deployment

## Assumptions

* The written tests are black-box tests, focusing on the external behavior of the application.
* The only change made to the application is the modification of input data.
* No additional intermediary infrastructure has been added, implying that the tests interact directly with the application without any intermediate components or systems.

## Tests Description:
* test_boundary:
  * Test if boundary lines were transferred to target hosts, to check if borderline were transferred 
* test_content:
  * Test to check if all lines were transferred correctly to target host
    * Assumption is files size will not exceed available memory
* test_duplicates:
  * Test to check if there are no duplicates in outputs from targets
    * Assumption is files size will not exceed available memory
* test_sum_lines:
  * Test to check if sum of lines in target outputs match input line count
* test_balancing:
  * Test to check if targets are evenly loaded
* test_throughput:
  * Test to measure throughput in lines and kb
* test_latency:
  * test to check latency between sending last line and writing it to target output