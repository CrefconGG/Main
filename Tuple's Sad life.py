"""Tuple's Sad life"""


def square():
    """Find this."""
    tup = tuple(input().split(" "))
    find = input()
    scale = tup.count(find)
    pen = tup.index(find)
    for _ in range(scale):
        for _ in range(scale):
            print(pen, end=" ")
        print()

square()
