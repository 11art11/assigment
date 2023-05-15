import json

def replace_json_value(json_file_path, key, new_value):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Change the value of the "monitor" key
    data[key] = new_value

    # Save the modified JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file)