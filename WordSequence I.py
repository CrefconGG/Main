"""WordSequence I"""


def over(word):
    """Find this."""
    _ = [print(word[:i]) for i in range(1, len(word) + 1)]

over(input())
