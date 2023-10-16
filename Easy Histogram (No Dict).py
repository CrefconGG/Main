"""Easy Histogram"""


def easy():
    """Find this."""
    cha = []
    word = input().replace(" ", "")
    cha.extend(word)
    onecha = cha.copy()
    onecha = list(set(onecha))
    onecha = sorted(onecha, key=sort)
    for i in onecha:
        num = cha.count(i)
        print(i, "=", num)

def sort(word):
    """Sorting this."""
    if ord(word) >= 97:
        return ord(word)
    else:
        return ord(word) + 32.5

easy()
