#!/usr/bin/python3
"""
Module to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads data from a CSV file and converts it into a JSON file."""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
