import tarfile


class TarGzExtractor:
    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self, output_path="."):
        with tarfile.open(self.filepath, "r:gz") as tar:
            tar.extractall(output_path)
