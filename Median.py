"""Median"""

def middle():
    """Find this."""
    medians = []
    nums = int(input())
    for _ in range(nums):
        numbers = int(input())
        medians.append(numbers)
    medians.sort()
    len_md = len(medians)
    if nums % 2 == 0:
        median1 = medians[len_md//2]
        median2 = medians[len_md//2 - 1]
        median = (median1 + median2)/2
        print(median)
    else:
        median = medians[len_md//2]
        print("%.1f" % (median))

middle()
