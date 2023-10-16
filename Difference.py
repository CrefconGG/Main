"""Difference"""


def sets():
    """Find this."""
    a_set = int(input())
    b_set = int(input())
    set_a = {int(input()) for _ in range(a_set)}
    set_b = {int(input()) for _ in range(b_set)}
    set_ab = sorted(set_a.difference(set_b))
    for i in set_ab:
        print(i, end=" ")

sets()
