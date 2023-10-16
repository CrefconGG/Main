"""Point Sorting"""


def point():
    """Find this."""
    list_data = []
    list_get = []
    set_data = int(input())

    for _ in range(set_data):
        num_data = int(input())
        for _ in range(num_data):
            data = input()
            data = list(map(int, data.split(" ")))
            list_get.append(data)
        data = sorted(list_get, key=key)
        list_data.extend(data)
        list_get = []
    for i in list_data:
        print(" ".join(map(str, i)))


def key(list_get):
    """Setting this."""
    return (list_get[0] + list_get[1], -int(list_get[1]))



point()
