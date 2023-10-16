"""BookWorm"""


def read():
    """Find this."""
    get_num = []
    count = 0
    set_time = 0.00
    set_book = int(input())
    for _ in range(set_book):
        time = float(input())
        books = int(input())
        count = 0
        set_time = 0
        get_num = []
        for _ in range(books):
            minute = float(input())
            get_num.append(minute)
        get_num.sort()
        for i in get_num:
            set_time += i
            if set_time <= time:
                count += 1
            else:
                break
        print(count)


read()
