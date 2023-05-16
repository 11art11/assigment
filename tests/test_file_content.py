from helpers.linecounter import get_line_count


def test_boundary(setup):
    # List of target files to search for lines
    target_filenames = ['./target_1_mount/events.log', './target_2_mount/events.log']
    # List of lines to search for
    lines_to_find = []
    # List of lines that were found in target files
    found_lines = []

    # Open the source file and read its lines
    with open(f"./cribl/assignment/agent/inputs/{setup}_events.log", 'r') as file:
        lines = file.readlines()
        # Add the first, last and middle lines to the list of lines to search for
        lines_to_find.append(lines[0])
        lines_to_find.append(lines[-1])
        lines_to_find.append(lines[len(lines) // 2])

    # Search for each line in the target files
    for filename in target_filenames:
        with open(filename, 'r') as file:
            file_lines = file.readlines()
            for line in lines_to_find:
                if line in file_lines:
                    found_lines.append(line)

    # Assert that all lines were found in the target files
    assert len(found_lines) == len(
        lines_to_find), f"Not all lines were found in target files, lost lines {list(set(lines_to_find) - set(found_lines))} "


def test_content(setup):
    """
    Test that all lines in the input file are found in the target files.
    Limitation: The test will not work for files that exceed the available memory.
    """
    # Read input file and target files into sets
    input_file = set(line.strip() for line in open(f'./cribl/assignment/agent/inputs/{setup}_events.log'))
    target_1 = set(line.strip() for line in open('./target_1_mount/events.log'))
    target_2 = set(line.strip() for line in open('./target_2_mount/events.log'))

    # Combine target sets into one set
    output = target_1.union(target_2)

    # Find lines in input file that are not in target set
    lost_lines = input_file - output

    # Check if there are any lost lines
    assert len(lost_lines) == 0, f"Not all lines were found in target files, lines lost no {len(lost_lines)}, lost " \
                                 f"line list: {lost_lines} "


def test_duplicates(setup):
    """
    Test that there are no duplicate entries in the target files.
    Limitation: The test will not work for files that exceed the available memory.
    """
    # file names of the files whose entries will be compared
    target1_log = './target_1_mount/events.log'
    target2_log = './target_2_mount/events.log'

    # read the contents of the files into lists
    with open(target1_log, 'r') as f1:
        entries1 = f1.readlines()
    with open(target2_log, 'r') as f2:
        entries2 = f2.readlines()

    # check if the entries in both files are unique
    duplicates = set(entries1) & set(entries2)
    assert not duplicates, f'Found duplicate entries: {duplicates}'


def test_sum_lines(setup):
    """
    Test that the number of lines in the output files matches the number of lines in the input file.
    """
    target1_lines = get_line_count('./target_1_mount/events.log')
    target2_lines = get_line_count('./target_2_mount/events.log')
    input_file_line_count = get_line_count(f'./cribl/assignment/agent/inputs/{setup}_events.log')
    assert target1_lines + target2_lines == input_file_line_count, \
        f"Line count mismatch: target1={target1_lines}, target2={target2_lines}, input={input_file_line_count}"


def test_balancing(setup):
    """
    Test that the number of lines in the output files matches the number of lines in the input file.
    """
    target1_lines = get_line_count('./target_1_mount/events.log')
    target2_lines = get_line_count('./target_2_mount/events.log')
    input_file_line_count = get_line_count(f'./cribl/assignment/agent/inputs/{setup}_events.log')
    line_count_diff = abs(target1_lines - target2_lines)
    assert line_count_diff < 0.02 * input_file_line_count, \
        f"Line count difference too large: {line_count_diff / input_file_line_count * 100}%"
