from helpers.directory import Directory
from decorators.decorators import *

class LogCreator:
    def __init__(self, log_length):
        self.log_length = log_length
    @timer
    def create_logs(self):
        for length in self.log_length:
            with open(f"../test_input/log_{length}_events.txt", "w") as f:
                for i in range(length):
                    f.write(f"This is event number {i + 1}\n")
            print(f"Created log_{length}_events.txt with {length} lines.")


directory = Directory("../test_input")
directory.create_directory()
log_creator = LogCreator(log_length=[100, 1000, 10000, 100000, 1000000, 100000000])
log_creator.create_logs()
