#!/usr/bin/python3
"""
Module that contains a function to convert an object to JSON
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
