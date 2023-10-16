"""Filter.py"""
import json


def student():
    """Find this."""
    count = 0
    idstd = json.loads(input().replace("'", '"'))
    passed = float(input())
    idstd = dict(sorted(idstd.items(), key=lambda x: x[0]))
    for key, value in idstd.items():
        if value >= passed:
            count += 1
            print(key + "\t" + "%.2f" % value)
    if count == 0:
        print("Nope")


student()
