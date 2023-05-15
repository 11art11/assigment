import os


class DockerComposeLogManager:
    def __init__(self, compose_file_path, log_file_path):
        self.compose_file_path = compose_file_path
        self.log_file_path = log_file_path

    def save_logs_to_file(self, since=None):
        since_str = f"--since '{since}'" if since else ""
        os.system(
            f"docker-compose -f {self.compose_file_path} logs -t --no-color {since_str} >> {self.log_file_path}")
        with open(self.log_file_path, 'r') as file:
            content = file.readlines()
            for line in content:
                print(line)



