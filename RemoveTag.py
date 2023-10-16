"""RemoveTag"""


def cleaner():
    """Find this."""
    inside = False
    html = input()
    my_list = []
    results = []
    final = []
    for i in html:
        if i == "<":
            inside = True
        elif i == ">":
            inside = False
            if my_list:
                results.append("".join(my_list))
                my_list = []
        elif not inside:
            my_list.append(i)
    if my_list:
        results.append("".join(my_list))
    for i in results:
        final.extend(str(i).split())
    print(final)


cleaner()
