import urllib.request


class FileDownloader:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download(self):
        def reporthook(count, block_size, total_size):
            """Callback function to report download progress."""
            percent = int(count * block_size * 100 / total_size)
            print(f"Downloading... {percent}%")

        print(f"Downloading {self.url} to {self.filename}...")
        urllib.request.urlretrieve(self.url, self.filename, reporthook=reporthook)
        print("Download complete.")