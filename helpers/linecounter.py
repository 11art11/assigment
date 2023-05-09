def get_line_count(file_path):
    # Get the number of lines in the file.
    with open(file_path, 'r') as input_file:
        file_line_count = sum(1 for line in input_file)
    return file_line_count
