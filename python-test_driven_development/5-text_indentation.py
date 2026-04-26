#!/usr/bin/python3
"""Module that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    simvollar = [".", "?", ":"]
    setr = ""

    i = 0
    while i < len(text):
        setr += text[i]
        if text[i] in simvollar:
            print(setr.strip())
            print()
            setr = ""
        i += 1
    if setr.strip():
        print(setr.strip(), end="")
