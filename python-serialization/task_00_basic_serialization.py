#!/usr/bin/python3
"""
asdfghjkl
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    asdfghjkl
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    asdfghjkl
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
