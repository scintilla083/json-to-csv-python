import json

import re
import time

class FileUsage:

    def __init__(self, file_path):
        self.file_path = file_path

    
    def line_reader(self):
        """
        Read lines from file, work with line-by-line json_data format
        :return:
        str(line)
        """
        with open(self.file_path, 'r') as raw_json:
            for line in raw_json:
                yield line.strip() + '\n'

    
    def file_reader(self):
        """
        read file and return json_data
        :return:
        json_data
        """
        with open(self.file_path) as file:
            json_data = json.loads(file.read())
        return json_data

    
    def raw_file_reader(self):
        """
        read file like text and return it
        :return:
        str
        """
        with open(self.file_path) as file:
            text = file.read()
            return text

    
    def raw_file_writer(self):
        """
        write file like text, and this case text is file_fixer (ln56)
        :return:
        NO RETURN, update file
        """
        text = self.file_fixer()
        with open(self.file_path, 'w') as file:
            file.write('')
            file.write(text)

    @staticmethod
    def file_writer(output, df):
        df.to_csv(output)

    def file_fixer(self):
        """
        fix json_data by adding '[' and ']', fix missing ','
        :return:
        str (full fixed json in str type)
        """
        text = self.raw_file_reader()
        if not text.startswith('['):
            text = '[' + text
        if not text.endswith(']'):
            text = text + ']'
        pattern = re.compile(r'}\s*{')
        modified_text = re.sub(pattern, '}, {', text)
        return modified_text
