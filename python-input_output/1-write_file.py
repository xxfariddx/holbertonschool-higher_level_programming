#!/usr/bin/python3
"""
Module that contains a function to write to a file
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns char count"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
