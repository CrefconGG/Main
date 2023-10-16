"""CaesarV1"""


def ordd():
    """Find htis."""
    letter = ""
    num = int(input()) % 26
    word = input()
    for i in word:
        if i.isupper() and i.isalpha():
            if (ord(i) + num) < 65:
                letter += chr(91 - (65 - (ord(i) + num)))
            elif (ord(i) + num) > 90:
                letter += chr(64 + ((ord(i) + num) - 90))
            else:
                letter += chr(ord(i) + num)
        elif i.islower() and i.isalpha():
            if (ord(i) + num) < 97:
                letter += chr(123 - (97 - (ord(i) + num)))
            elif (ord(i) + num) > 122:
                letter += chr(96 + ((ord(i) + num) - 122))
            else:
                letter += chr(ord(i) + num)
        else:
            letter += i
    print(letter)

ordd()
