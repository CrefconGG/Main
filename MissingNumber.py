"""MissingNumber"""


def findnum():
    """Find this."""
    top = int(input())
    set_num = set()
    all_num = set(range(1, top + 1))
    while True:
        num = int(input())
        if num == 0:
            break
        set_num.add(num)
    _ = [print(i) for i in sorted(all_num.difference(set_num))]

findnum()
