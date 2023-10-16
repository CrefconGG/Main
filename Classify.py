"""Classify"""


def idstudent():
    """Find this."""
    std = []

    while True:
        iden = input()
        if iden == "END":
            break
        std.append(iden[:4])
    std.sort(key=sort)
    stdx = list(set(std.copy()))
    stdx.sort(key=sort)

    head = []

    for i in stdx:
        if i[:2] != head[:2]:
            print(i[:2], int(i[2:]), std.count(i))
            head = i
        elif i[:2] == head[:2] and i[2:] != head[2:]:
            print("--", int(i[2:]), std.count(i))

def sort(std):
    """Sorting this."""
    return std[:2], std[2:4]


idstudent()
