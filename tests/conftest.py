from helpers.filedownloader import FileDownloader
from helpers.targzextractor import TarGzExtractor
from helpers.directory import create_directory
from docker_utils.dockercompose import DockerCompose
from docker_utils.dockercomposelogs import DockerComposeLogManager
import ssl
from helpers.fileobserver import observe_directories
import pytest
from datetime import datetime
from helpers.archiver import *

#todo multiple parameter
@pytest.fixture(scope="session", params=[100,10000,1000000])
def setup():
    ssl._create_default_https_context = ssl._create_unverified_context
    create_directory(['./target_1_mount', './target_2_mount', './artifacts', './cribl'])
    setup = Setup("https://drive.google.com/u/0/uc?id=16k1na8UA0THRBQbKSeo8t_spX1ehkXwx&export=download",
                  "./assigment.tar.gz")
    setup.download_and_extract(output_path="./cribl")
    setup.docker("start")
    observe_directories('./target_1_mount', './target_2_mount', './artifacts/target_1.txt', './artifacts/target_2.txt')
    setup.docker_compose_logs()
    yield
    setup.archive()
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
        # todo remove hardcode
        docker_compose = DockerCompose('./docker-compose.yml')
        if action == "start":
            docker_compose.start()
        elif action == "down":
            docker_compose.down()

    def docker_compose_logs(self):
        log_manager = DockerComposeLogManager("./docker-compose.yml", "./artifacts/docker-compose-logs.txt")
        log_manager.save_logs_to_file()

    def archive(self):
        archiver = TestArtifactArchiver('./')
        archiver.archive_artifacts(['./target_1_mount', './target_2_mount', './artifacts'], f'test_archive_{datetime.utcnow()}_zip')
