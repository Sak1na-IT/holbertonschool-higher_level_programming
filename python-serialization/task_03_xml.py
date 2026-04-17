#!/usr/bin/python3
"""
asdfghjkl
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    asdfghjkl
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    asdfghjkl
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        res = {}
        for child in root:
            res[child.tag] = child.text

        return res
    except Exception:
        return None
