"""Backward"""


def backward():
    """Find this."""
    word_list = []
    while True:
        text = input()
        if text == "NULL":
            break
        word_list.append(text)
    word_list.reverse()
    for i in word_list:
        print(i)


backward()
