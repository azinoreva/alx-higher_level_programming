#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

       Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    p = 0
    while p < len(text) and text[p] == ' ':
        p += 1

    while p < len(text):
        print(text[p], end="")
        if text[p] == "\n" or text[p] in ".?:":
            if text[p] in ".?:":
                print("\n")
            p += 1
            while p < len(text) and text[p] == ' ':
                p += 1
            continue
        p += 1
