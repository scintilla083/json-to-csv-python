import argparse
from utils.convert import Converter
from utils.checker import TypeChecker
import os
import time

def main():
    parser = argparse.ArgumentParser(description='Process JSON files and convert them to CSV.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')

    args = parser.parse_args()

    print(f'{args.input_file} --- {time.strftime("%H:%M:%S", time.localtime())}')

    checker = TypeChecker(file_path=args.input_file)
    result = checker.check()

    converter = Converter(result=result, output=args.output_file)
    converter.convert()

if __name__ == "__main__":
    main()
