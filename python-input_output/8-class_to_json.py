#!/usr/bin/python3
"""
Module that contains a function that returns the dictionary 
description of an object for JSON serialization
"""


def class_to_json(obj):
    """Returns the dictionary description of an obj instance"""
    return obj.__dict__
