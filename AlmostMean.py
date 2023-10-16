"""AlmostMean"""


def isclose():
    """Find this."""
    nums = int(input())
    original = []
    no_score = []
    score = []
    point = 0
    for i in range(nums):
        score_no = input()
        no_score.extend(score_no.split())
        original.append(score_no)
    no_score = list(map(float, no_score))
    for i in range(len(no_score)):
        if i % 2 != 0:
            point += no_score[i]
            score.append(no_score[i])
    mean = point / nums
    first = 0
    for i in score:
        if i > first and i <= mean:
            first = i
    locate = score.index(first)
    print(original[locate])


isclose()
