"""isprime_small"""


def itself():
    """Find this."""
    prime = 0
    num = int(input())
    for i in range(1, num + 1):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            prime += 1
    print(prime)

itself()
