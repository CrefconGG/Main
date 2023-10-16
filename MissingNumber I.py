"""MissingCard (No Set)"""


def card():
    """Find this."""
    all_card = {rank + types if rank != "T" else "10" + types\
    for rank in "23456789TJQKA"  for types in "SHDC"}
    lost_card = {input() for x in range(51)}
    print((all_card.difference(lost_card)).pop())

card()
