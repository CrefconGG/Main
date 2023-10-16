"""VerticalHistogram"""


def asterisk(word):
    """Find this."""
    result = {}
    for i in word:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    alpha = sorted(result.keys(), key=lambda x: ord(x) if ord(x) > 96 else ord(x) + 57.5)
    top = max(result.values())
    for i in range(top, 0, -1):
        print("{:03d}".format(i), end=" ")
        for j in alpha:
            if result.get(j) >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("    " + " ".join(alpha))




asterisk(input())
