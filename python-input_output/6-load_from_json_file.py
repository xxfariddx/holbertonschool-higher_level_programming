#!/usr/bin/python3
"""
Module that contains a function to load an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
