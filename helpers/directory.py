import os
import shutil


def create_directory(paths):
    """
    Creates the directory specified by the path.

    If the directory already exists, it will first delete it and then recreate it.
    """
    for path in paths:
        if os.path.exists(path):
            shutil.rmtree(path)  # Remove existing directory if it exists
        os.mkdir(path)  # Create the directory
