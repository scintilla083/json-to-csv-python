from utils.convert import Converter
from utils.checker import TypeChecker
import os
import time

folder_path = "tests"

#https://github.com/jdorfman/awesome-json-datasets/tree/master?tab=readme-ov-file
files_in_folder = os.listdir(folder_path)

for file_name in files_in_folder:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f'{file_name} --- {current_time}')
    checker = TypeChecker(file_path='tests/{}'.format(file_name))
    result = checker.check()                                      
    converter = Converter(result=result, output='output/{}.csv'.format(file_name))
    converter.convert()

















"""
raw_list = [json.loads(line) for line in line_reader()]
df_rows = pd.json_normalize(raw_list)
df = pd.DataFrame(df_rows)

raw_list = [json.loads(line) for line in line_reader()]

"""

"""
def main():
    def line_reader():
        with open('gear/order.bson.json', 'r') as raw_json:
            for line in raw_json:
                yield line.strip() + '\n'

    raw_list = [json.loads(line) for line in line_reader()]
    df_rows = pd.json_normalize(raw_list)
    df = pd.DataFrame(df_rows)
    df.to_csv('gear/normalize 2 -3 line.csv')


if __name__ == '__main__':
    execution_time = timeit.timeit(main, number=1)
    print(f"Время выполнения: {execution_time} секунд")
"""