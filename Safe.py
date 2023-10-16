"""Safe"""


def password():
    """Find this."""
    decode = [input() for _ in range(2)]
    total = sum(abs(ord(i) - ord(j)) if abs(ord(i) - ord(j)) <= 13 else 26 - abs(ord(i) - ord(j))\
    for i, j in zip(decode[0], decode[1]))
    print(total)

password()
