"""PickThemAgain"""


def pickthem():
    """Find this."""
    text = input()
    text = text.split()
    text = list(map(int, text))
    text.reverse()
    count = 0
    for i in text:
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")
pickthem()
