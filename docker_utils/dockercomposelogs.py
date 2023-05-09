import os


class DockerComposeLogManager:
    def __init__(self, compose_file_path, log_file_path):
        self.compose_file_path = compose_file_path
        self.log_file_path = log_file_path

    def save_logs_to_file(self, since=None):
        since_str = f"--since '{since}'" if since else ""
        with open(self.log_file_path, 'w') as log_file:
            os.system(
                f"docker-compose -f {self.compose_file_path} logs -t --no-color {since_str} >> {self.log_file_path}")


