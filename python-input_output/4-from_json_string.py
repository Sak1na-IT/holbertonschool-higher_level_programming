#!/usr/bin/python3
"""
This module contains a function that returns an object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The Python data structure (list, dict, etc.).
    """
    return json.loads(my_str)
