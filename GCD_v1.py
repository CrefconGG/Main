"""GCD_v1"""


def gcd():
    """Find this"""
    num1 = int(input())
    num2 = int(input())
    while num2:
        num1, num2 = num2, num1 % num2
    print(num1)

gcd()
