#!/usr/bin/python3
"""fsdjf kdsfds sdf"""
import json


def serialize_and_save_to_file(data, filename):
    """ asd asf """

    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4)

def load_and_deserialize(filename):
    """sad asd"""

    with open(filename, encoding="UTF-8") as f:
        data = json.load(f)
    return data
