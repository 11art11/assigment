import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime


class MyHandler(FileSystemEventHandler):
    def __init__(self, log_file_path, input_file):
        super().__init__()
        self.last_modified_time = time.time()
        self.last_pos = 0  # Initialize last_pos to 0
        self.log_file_path = log_file_path
        self.input_file = input_file
        self.stop_line_found = False  # Track if the stop line is found

    def on_modified(self, event):
        # This method will be called whenever a file is modified in the observed directories
        if event.is_directory:
            # Ignore directory events
            return

        # Check if event.src_path is a file
        if not os.path.isfile(event.src_path):
            return

        # This method will be called whenever the file is modified

        with open(event.src_path, 'r') as f, open(self.log_file_path, 'a') as log_file, open(self.input_file, 'r') as input:
            stop_line = input.readlines()[-1]
            f.seek(self.last_pos)
            for line in f:
                timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
                log_line = f"[{timestamp}] {line.strip()}"
                log_file.write(log_line + '\n')
                if stop_line in line:
                    self.stop_line_found = True  # Set stop_line_found to True
                    return
            self.last_pos = f.tell()
        self.last_modified_time = time.time()

    def on_created(self, event):
        # This method will be called whenever the file is created
        with open(event.src_path, 'r') as f:
            self.last_pos = f.tell()
        self.last_modified_time = time.time()


def observe_directories(dir1_path, dir2_path, log_file_path, log_file_path_2, input_file):
    event_handler_1 = MyHandler(log_file_path, input_file)
    observer_1 = Observer()
    observer_1.schedule(event_handler_1, path=dir1_path, recursive=False)
    observer_1.start()

    event_handler_2 = MyHandler(log_file_path_2, input_file)
    observer_2 = Observer()
    observer_2.schedule(event_handler_2, path=dir2_path, recursive=False)
    observer_2.start()

    # Wait for changes and stop if there are no changes for 100 seconds
    while True:
        time.sleep(0.01)
        if time.time() - max(event_handler_1.last_modified_time, event_handler_2.last_modified_time) > 100 or \
                (event_handler_1.stop_line_found or event_handler_2.stop_line_found):
            observer_1.stop()
            observer_2.stop()
            break

    observer_1.join()
    observer_2.join()
