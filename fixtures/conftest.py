import threading
from helpers.filedownloader import FileDownloader
from helpers.replacevalueinjson import replace_json_value
from helpers.targzextractor import TarGzExtractor
from helpers.directory import create_directory
from helpers.archiver import *
from helpers.inputgenerator import *
from docker_utils.dockercompose import DockerCompose
from docker_utils.dockercomposelogs import DockerComposeLogManager
import ssl
from helpers.fileobserver import observe_directories
import pytest
from datetime import datetime


# Define the fixture with session scope and parameterized values
@pytest.fixture(scope="session", params=[100, 10000, 1000000])
def setup(request):
    # Create the Setup object with required configuration
    setup = Setup("https://drive.google.com/u/0/uc?id=16k1na8UA0THRBQbKSeo8t_spX1ehkXwx&export=download",
                  "./assigment.tar.gz")
    ssl._create_default_https_context = ssl._create_unverified_context
    create_directory(['./target_1_mount', './target_2_mount', './artifacts', './cribl'])

    # Download and extract the necessary files
    setup.download_and_extract(output_path="./cribl")

    # Generate log files based on the provided parameter
    setup.log_generator(request.param)

    # Replace a JSON value in the input file
    replace_json_value('./cribl/assignment/agent/inputs.json', 'monitor', f'inputs/{request.param}_events.log')

    # Start a separate thread for files observation
    thread = threading.Thread(target=observe_directories, args=(
    './target_1_mount', './target_2_mount', './artifacts/target_1.txt', './artifacts/target_2.txt',
    f'./cribl/assignment/agent/inputs/{request.param}_events.log'))
    thread.start()

    # Start the Docker containers
    setup.docker("start")

    # Wait for the observation thread to finish
    thread.join()

    # Save Docker Compose logs
    setup.docker_compose_logs()

    # Yield the parameter value for the test
    yield request.param

    # Archive the test artifacts
    setup.archive(['./target_1_mount', './target_2_mount', './artifacts', f'./cribl/assignment/agent/inputs/{request.param}_events.log'], f'test_archive_{request.param}_events_{datetime.utcnow()}_zip')

    # Stop and remove the Docker containers
    setup.docker("down")


class Setup:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download_and_extract(self, output_path="."):

        downloader = FileDownloader(self.url, self.filename)
        downloader.download()

        extractor = TarGzExtractor(self.filename)
        extractor.extract(output_path)

    def docker(self, action):
        docker_compose = DockerCompose('./docker-compose.yml')
        if action == "start":
            docker_compose.start()
        elif action == "down":
            docker_compose.down()

    def docker_compose_logs(self):
        log_manager = DockerComposeLogManager("./docker-compose.yml", "./artifacts/docker-compose-logs.txt")
        log_manager.save_logs_to_file()

    def archive(self, source_paths, zip_name):
        archiver = TestArtifactArchiver('../tests/')
        archiver.archive_artifacts(source_paths, zip_name)

    def log_generator(self, log_lenght):
        log_generator = LogCreator()
        log_generator.create_logs(log_lenght)
