"""GCD_v1"""


def gcd():
    """Find this"""
    num1 = int(input())
    num2 = int(input())
    while num2:
        num1, num2 = num2, num1 % num2
    if num1 == 1:
        print("YES\n%d" % (num1))
    else:
        print("NO\n%d" % (num1))

gcd()
