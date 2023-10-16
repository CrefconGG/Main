"""AscendingSort"""


def sort():
    """Find this"""
    my_list = []
    for _ in range(5):
        nums = int(input())
        my_list.append(nums)
    my_list.sort()
    for i in my_list:
        print(i)



sort()
