'''
Executable file for py-solc compiler
Execute - python py-solc.py
'''

import argparse
import subprocess

from parser import Parser
from lexer import Lexer

def main():
    '''
    todo: function to interact with the user
    Loads the input file and interacts with the user.
    '''
    arguments = get_args()

    try:
        with open(arguments.file_name) as sol_file:
            code = [
                (line_text.strip(), arguments.file_name, line_num + 1)
                for line_num, line_text in enumerate(sol_file)
            ]
    except IOError:
        pass

    asm_source = to_asm(code)
    asm_file = "out.s"
    write_asm(asm_source, asm_file)
    assemble_and_link("out", asm_file, "out.o")


def get_args():
    '''
    todo: function to set up the argument Parser
    sets up the argument parser and returns an object storing the arguments
    '''
    parser = argparse.ArgumentParser(description="Compiler solidity")
    parser.add_argument("file_name", metavar="filename")
    return parser.parse_args()


def to_asm(code):
    '''
    todo: function to compile the given code and give to asm
    '''
    return ""

def write_asm(asm_source, asm_file):
    '''
    todo: function to save the given assembly to disk
    '''
    try:
        with open(asm_file, "w") as c_file:
            c_file.write(asm_source)
    except IOError:
        pass


def assemble_and_link(binary, asm_file, obj):
    '''
    todo: function to assemble and link the file
    '''
    subprocess.check_call()
    subprocess.check_call()

if __name__ == "__main__":
    main()
