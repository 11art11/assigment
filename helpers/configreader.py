import configparser


class ConfigReader:
    def __init__(self, yaml_file_path):
        self.yaml_file_path = yaml_file_path
        self.config = configparser.ConfigParser()

    def read_config(self):
        # Read the YAML file as a plain text file
        with open(self.yaml_file_path, 'r') as file:
            yaml_text = file.read()

        # Convert YAML text to sections and options in ConfigParser
        self.config.clear()
        self.config.read_string(yaml_text)

    def get_value(self, section, option):
        # Get the value of an option from a section
        return self.config.get(section, option)
