"""Diamond I"""


def mine():
    """Find this."""
    diamond = []
    count = 0
    sums = 0
    height = int(input())
    width = int(input())
    for _ in range(height):
        diamond.append(input().split(" "))
    for i in range(width):
        for j in range(len(diamond)):
            count += int(diamond[j][i])
        if count >= sums:
            sums = count
        count = 0

    print(sums)

mine()
