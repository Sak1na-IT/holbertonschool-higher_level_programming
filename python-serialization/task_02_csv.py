#!/usr/bin/python3
"""
asdfghjkl
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    asdfghjkl
    """
    try:
        data = []
        with open(csv_filename, "r", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_f:
            json.dump(data, json_f)

        return True
    except Exception:
        return False
