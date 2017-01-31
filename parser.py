"""
Lexer for py-solc. To separate a stream of characters into Tokens.
"""

import  re

class Token:
    """
    A token is a single semantic unit in Solidity
    """
    def __init__(self, name):
        self.name = name