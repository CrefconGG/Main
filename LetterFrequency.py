"""LetterFrequency"""
import re


def letter():
    """Find this."""
    text = {}
    word = re.sub("[^A-Za-z0-9]+", "", input())
    for x_cha in word:
        if x_cha in text:
            text[x_cha] += 1
        else:
            text[x_cha] = 1
    print(max(text, key=text.get))

letter()
