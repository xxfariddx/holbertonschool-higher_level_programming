#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries to/from XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        deserialized_data = {}
        for child in root:
            deserialized_data[child.tag] = child.text

        return deserialized_data
    except (FileNotFoundError, ET.ParseError):
        return None
