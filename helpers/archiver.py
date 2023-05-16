import os
import zipfile


class TestArtifactArchiver:
    def __init__(self, artifacts_dir):
        self.artifacts_dir = artifacts_dir
        os.makedirs(self.artifacts_dir, exist_ok=True)

    def archive_artifacts(self, source_paths, archive_name):
        """
        Archives artifacts from given locations to a zip file with the given name.

        :param source_paths: list of paths to files or directories to be added to the archive
        :param archive_name: name of the archive file
        """
        archive_path = os.path.join(self.artifacts_dir, archive_name)

        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for path in source_paths:
                if os.path.isfile(path):
                    # Add a single file to the archive
                    zip_file.write(path, os.path.basename(path))
                elif os.path.isdir(path):
                    # Add the contents of a directory to the archive
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zip_file.write(file_path, os.path.join(os.path.relpath(path), file))
        print(f'Archive {archive_name} has been created in {self.artifacts_dir}')
