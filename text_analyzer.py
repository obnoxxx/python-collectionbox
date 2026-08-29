#!/usr/bin/env python3
"""
read text from stdin, count words, characters and frequencies of different characters.
"""

import sys

from collectionbox import Chain


def char_display(char):
    """
    Display special characters with their representation
    """
    if char == " ":
        display_char = "<space>"
    elif char == "\n":
        display_char = "<newline>"
    elif char == "\t":
        display_char = "<tab>"
    else:
        display_char = char
    return display_char


text = sys.stdin.read()

words = text.split()

characters = Chain()
different_characters = Chain()

for character in text:
    characters.append(character)
    if different_characters.count(character) == 0:
        different_characters.append(character)

print("num words:", len(words))
print("num chars:", len(text))
print("num different chars:", len(different_characters))

print("character frequencies:")
print("-" * 40)
print(f"{'Character':<15} {'Count':>10}")
print("-" * 40)
for char in sorted(different_characters, key=characters.count, reverse=True):
    display_char = char_display(char)
    count = characters.count(char)
    print(f"{display_char:<15} {count:>10}")

print("-" * 40)
