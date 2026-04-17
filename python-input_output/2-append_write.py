#!/usr/bin/python3
"""
Module that contains a function to append to a file
"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns char count"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
