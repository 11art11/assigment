import os
from helpers.linecounter import get_line_count
from helpers.readtimestamp import *


def agent_start_timestamp():
    with open('./artifacts/docker-compose-logs.txt', 'r') as file:
        for line in file:
            if 'agent' in line and 'connected to target' in line:
                agent_start = extract_docker_compose_log_timestamp(line)
                break
    return agent_start


def agent_down_timestamp():
    with open('./artifacts/docker-compose-logs.txt', 'r') as file:
        for line in file:
            if 'agent exited' in line:
                agent_stop = extract_docker_compose_log_timestamp(line)
                break
    return agent_stop


# define the last_event_timestamp function
def last_event_timestamp(input_file):
    # open the log file and get its last line
    with open(input_file, 'r') as f1:
        last_line = f1.readlines()[-1]

    # open the first target file and get its last line
    with open('./artifacts/target_1.txt', 'r') as f1:
        last_line_target1 = f1.readlines()[-1]

    # open the second target file and get its last line
    with open('./artifacts/target_2.txt', 'r') as f1:
        last_line_target2 = f1.readlines()[-1]

    # check which target file contains the last line of the log file and extract the event timestamp
    if last_line in last_line_target1:
        last_event = extract_events_log_timestamp(last_line_target1)
    elif last_line in last_line_target2:
        last_event = extract_events_log_timestamp(last_line_target2)
    else:
        # if neither target file contains the last line, extract the timestamps from both target files and return the max
        last_event = max(extract_events_log_timestamp(last_line_target1),
                         extract_events_log_timestamp(last_line_target2))

    # return the timestamp of the last event
    return last_event


def test_throughput(setup):
    """
    Test throughput in lines/ms and kb/ms
    """
    # get the size of the input file in kilobytes
    input_file_size = os.path.getsize(f'./cribl/assignment/agent/inputs/{setup}_events.log') / 1024

    # get the number of lines in the input file
    input_file_lines = get_line_count(f'./cribl/assignment/agent/inputs/{setup}_events.log')

    # calculate the time it took to transfer the log file, in milliseconds
    transfer_time_ms = int((last_event_timestamp(
        f'./cribl/assignment/agent/inputs/{setup}_events.log') - agent_start_timestamp()).total_seconds() * 1000)

    # calculate the transfer rate in lines per millisecond
    transfer_lines = input_file_lines / transfer_time_ms

    # calculate the transfer rate in kilobytes per millisecond
    transfer_kb = input_file_size / transfer_time_ms

    # assert that the transfer rate is greater than 10 lines per millisecond
    assert transfer_lines > 10, f'Transfer rate lower than 10 lines per ms: {transfer_lines}'

    # assert that the transfer rate is greater than 0.25 kilobytes per millisecond
    assert transfer_kb > 0.25, f'Transfer rate lower than 0.25kb/ms : {transfer_kb}'


# define the test_latency function
def test_latency(setup):
    """
    Test latency
    """
    # calculate the latency between the last event timestamp and the agent down timestamp, in milliseconds
    latency_ms = int((last_event_timestamp(
        f'./cribl/assignment/agent/inputs/{setup}_events.log') - agent_down_timestamp()).total_seconds() * 1000)

    # assert that the latency is less than 100 milliseconds
    assert latency_ms < 100, f'Latency bigger than 100ms: {latency_ms}'
