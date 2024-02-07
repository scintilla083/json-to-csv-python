from .file_util import FileUsage
import json

import time


class TypeChecker:
    def __init__(self, file_path):
        self.file_instance = FileUsage(file_path=file_path)


    def check(self):
        """
        check json file type and return it with bool , also return json_data to speed up code
        :return:
        [Bool, list[]]
        """
        try:
            raw_list = [json.loads(line) for line in self.file_instance.line_reader()]
            return True, raw_list

        except json.JSONDecodeError:
            try:
                json_data = self.file_instance.file_reader()
                return False, json_data

            except json.JSONDecodeError:
                try:
                    self.file_instance.raw_file_writer()
                    json_data = self.file_instance.file_reader()
                    return False, json_data
                except json.JSONDecodeError:
                    return "No valid json"

