from helpers.filedownloader import FileDownloader
from helpers.targzextractor import TarGzExtractor
from helpers.directory import create_directory
from docker_utils.dockercompose import DockerCompose
from docker_utils.dockercomposelogs import DockerComposeLogManager
import ssl
from helpers.fileobserver import observe_directories
import pytest

#todo multiple parameter
@pytest.fixture(scope="session")
def setup():
    ssl._create_default_https_context = ssl._create_unverified_context
    create_directory('./target_1_mount')
    create_directory('./target_2_mount')
    create_directory('./artifacts')
    setup = Setup("https://drive.google.com/u/0/uc?id=16k1na8UA0THRBQbKSeo8t_spX1ehkXwx&export=download",
                  "./assigment.tar.gz")
    setup.download_and_extract(output_path="./cribl")
    setup.docker("start")
    observe_directories('./target_1_mount', './target_2_mount', './artifacts/target_1.txt', './artifacts/target_2.txt')
    setup.docker_compose_logs()
    yield
    # setup.docker("down")


class Setup:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download_and_extract(self, output_path="."):
        create_directory(output_path)

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
# setup:
#     download
#     uzip
#     create docker
# test:
#     czyszczenie logow
#     podmiana danych
#     zebranie artefaktow - archive logs
#     odpalenie testow
# teardown:
#     docker down

# for plik w pliki:
#     wycyzsc logi
#     podmien input
#     wystartuj agenta
# time.sleep(3)
# wez ostatnia linijke z input.log
# monitoring target hosts to catch timestamp of last line
# fetch from docker_compose logs timestamps when agent start & stop
# setup.get_target_files()
# setup.docker("down")
