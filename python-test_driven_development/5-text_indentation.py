#!/usr/bin/python3
"""
This module provides a function for text indentation.
It adds two new lines after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger a double newline
    delimiters = [".", "?", ":"]

    i = 0
    # Strip leading whitespace from the start of the entire text
    text = text.strip(" ")

    while i < len(text):
        print(text[i], end="")
        if text[i] in delimiters:
            print("\n")
            # Skip all subsequent spaces after a delimiter
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
