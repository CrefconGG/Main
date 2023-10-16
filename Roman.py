"""Roman"""


def calcu():
    """Find this."""
    real_num = 0
    before = 0
    num_of_roman = {"I": 1, "V": 5,
                    "X": 10, "L": 50,
                    "C": 100, "D": 500,
                    "M": 1000}
    romnum = input()
    for i in reversed(romnum):
        if num_of_roman.get(i) < before:
            real_num -= num_of_roman.get(i)
        else:
            real_num += num_of_roman.get(i)
            before = num_of_roman.get(i)
    print(real_num)

calcu()
