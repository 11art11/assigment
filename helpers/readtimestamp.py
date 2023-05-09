from datetime import datetime


def extract_events_log_timestamp(text_line):

    # Extract the timestamp substring
    timestamp_str = text_line[1:24]

    # Convert the timestamp string into a datetime object
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')

    # Return the extracted timestamp
    return timestamp


def extract_docker_compose_log_timestamp(text_line):
    # Split the text line by '|'
    parts = text_line.split('|')

    # Extract the timestamp substring from the second part of the text line
    timestamp_str = parts[1].split()[0].strip()

    # Convert the timestamp string into a datetime object
    timestamp = datetime.strptime(timestamp_str[:26], '%Y-%m-%dT%H:%M:%S.%f')

    # Return the extracted timestamp
    return timestamp

