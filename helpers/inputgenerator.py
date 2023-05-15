# from helpers.directory import Directory
from decorators.decorators import *

class LogCreator:
    def __init__(self):
        pass
    @timer
    def create_logs(self, log_length):
        with open(f"./cribl/assignment/agent/inputs/{log_length}_events.log", "w") as f:
            for i in range(log_length):
                f.write(f"This is event number {i + 1}\n")
        print(f"Created {log_length}_events.log with {log_length} lines.")


# directory = Directory("../test_input")
# directory.create_directory()
# log_creator = LogCreator()
# log_creator.create_logs()
