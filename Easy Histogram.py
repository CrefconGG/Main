"""Easy Histogram"""


def easy():
    """Find this."""
    word = input().replace(" ", "")
    cha = {}
    for i in word:
        if i in cha:
            cha[i] += 1
        else:
            cha[i] = 1
    onecha = sorted(list(cha.keys()), key=sort)
    for j in onecha:
        print(j, "=", cha[j])


def sort(word):
    """Sorting this."""
    if ord(word) >= 97:
        return ord(word)
    else:
        return ord(word) + 32.5

easy()
