"""isprime_small"""


def itself():
    """Find this."""
    isprime = "Yes"
    num = int(input())
    for i in range(2, num):
        if num % i == 0:
            isprime = "No"
            break
    if num == 1 or num == 0:
        isprime = "No"
    print(isprime)

itself()
