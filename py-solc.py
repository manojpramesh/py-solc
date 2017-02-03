'''
Executable file for py-solc compiler
Execute - python py-solc.py
'''

import argparse

from parser import Parser 
from lexer import Lexer 

def main():
    # TODO: function to interact with the user
    # Loads the input file and interacts with the user.
    arguments = ger_args()
    
    try:
        with open(arguments.file_name) as sol_file:
            code = [
                (line_text.strip(), arguments.file_name, line_num + 1)
                for line_num, line_text in enumerate(sol_file)
            ]
    except IOError:
        pass


def get_args():
    # TODO: function to set up the argument Parser
    # sets up the argument parser and returns an object storing the arguments
    
    parser = argparse.ArgumentParser(description="Compiler solidity")
    parser.add_argument("file_name",metavar="filename")
    return parser.parse_args()


def to_asm():
    # TODO: function to compile the given code and give to asm


def write_asm():
    # TODO: function to save the given assembly to disk


def assemble_and_link():
    # TODO: function to assemble and link the file


if __name__ == "__main__":
    main()
