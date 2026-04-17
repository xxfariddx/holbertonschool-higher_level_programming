#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file.
"""
import sys

# Importing our previous functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Load existing items if the file exists
try:
    items = load_from_json_file(filename)
except Exception:
    items = []

# 2. Add all arguments (starting from index 1) to the list
# sys.argv[0] is the script name, so we skip it.
items.extend(sys.argv[1:])

# 3. Save the updated list back to the file
save_to_json_file(items, filename)
