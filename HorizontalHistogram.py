"""HorizontalHistogram"""


def mos():
    """Find this."""
    cha = {}
    word = input()
    for i in word:
        if i in cha:
            cha[i] += 1
        else:
            cha[i] = 1
    cha = dict(sorted(cha.items(), key=lambda alpha: (ord(alpha[0]) + 57.5)\
     if (ord(alpha[0]) < 97) else ord(alpha[0])))
    for key, value in cha.items():
        print(key, ":", end=" ")
        for i in range(1, value + 1):
            print("-", end="")
            if i % 5 == 0 and i != value:
                print("|", end="")
        print()

mos()
