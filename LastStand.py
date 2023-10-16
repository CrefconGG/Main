"""LastStand"""
import json

def lastfirst():
    """Find this."""
    text = input()
    text = json.loads(text)
    for i in text:
        text = str(i)
        print(text[-1])


lastfirst()
