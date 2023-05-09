import subprocess
import time


class DockerCompose:
    """
    Class for starting and stopping a Docker Compose file.
    """

    def __init__(self, path):
        """
        Initialize the class.

        :param path: The path to the Docker Compose file.
        """
        self.path = path

    def start(self):
        """
        Start the Docker Compose file.
        """
        try:
            subprocess.run(['docker-compose', '-f', self.path, 'up', '-d'])
            print('Docker Compose has been started.')
        except Exception as e:
            print(f'An error occurred while starting Docker Compose: {e}')

    def stop(self):
        """
        Stop the Docker Compose file.
        """
        try:
            subprocess.run(['docker-compose', '-f', self.path, 'stop'])
            print('Docker Compose has been stopped.')
        except Exception as e:
            print(f'An error occurred while stopping Docker Compose: {e}')

    def down(self):
        """
        Stop and remove the Docker Compose file.
        """
        try:
            subprocess.run(['docker-compose', '-f', self.path, 'down', '-v'])
            print('Docker Compose has been stopped and removed.')
        except Exception as e:
            print(f'An error occurred while stopping Docker Compose: {e}')
