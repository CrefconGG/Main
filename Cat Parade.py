"""Cat Parade"""

def catmoew():
    """Find this."""
    my_list = []
    him_list = []
    her_list = []
    our_list = []
    text = "cat"
    while True:
        text = input()
        if text == "END":
            break
        my_list.append(text.split(", "))
    for i in my_list:
        him_list.extend(i)
    for i in him_list:
        if i == "IT'S A DOG":
            her_list.pop(-1)
            our_list.pop(-1)
        if i != "IT'S A DOG":
            her_list.append(i)
            our_list.append(i)
    thier_list = list(set(her_list))
    thier_list.sort()
    for i in thier_list:
        nums = our_list.index(i)
        count = our_list.count(i)
        print(i, nums + 1, count)


catmoew()
