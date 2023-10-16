"""PickThem"""
import json

def jason():
    """Find this."""
    lists = input()
    count = 0
    lists = json.loads(lists)
    for i in lists:
        if i % 2 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")


jason()
