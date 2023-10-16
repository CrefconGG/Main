"""Muddled Menu"""

def restuarant():
    """Find this."""
    menu = []
    back = []
    while True:
        word = input()
        if word == "DONE":
            break
        elif "#" in word and word[-1] != "N":
            word = word.split(" #")
            menu.insert(int(word[1]) - 1, word[0])
        elif word[-1] == "N":
            menu.append(word[:-3])
        elif word == "SOMETHING'S WRONG":
            menu.clear()
        elif "Can't do: " in word:
            menu.remove(word[10:])
        elif word == "CLOSED":
            menu.clear()
            break
    back = menu.copy()
    back.reverse()

    print("Full Course: {0} Reversed: {1}".format(menu, back))

restuarant()
