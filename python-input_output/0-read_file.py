#!/usr/bin/python3
"""
Module that contains a function to read a file
"""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
