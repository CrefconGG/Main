"""Seeker"""
import re


def seen():
    """Find this."""
    text = re.findall(r"\d+", input())
    print(sum(int(x) for x in text))

seen()
