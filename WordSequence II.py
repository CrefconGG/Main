"""WordSequence II"""


def hardthink(word1, word2):
    """Find this."""
    _ = [print(word2[:i] + word1[i:]) for i in range(max(len(word1), len(word2)) + 1)]

hardthink(input(), input())
