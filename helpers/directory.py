import os
#
#
# class Directory:
#
#     def __init__(self, path):
#         """
#         Constructor for Directory class.
#
#         Parameters:
#             path (str): The path to the directory.
#         """
#         self.path = path

def create_directory(path):
    """
    Creates the directory specified by the path.

    If the directory already exists, it will first delete it and then recreate it.
    """
    if os.path.exists(path):
        os.rmdir(path)  # Remove existing directory if it exists
    os.mkdir(path)  # Create the directory
