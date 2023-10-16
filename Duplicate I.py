"""Duplicate I"""


def sets(m_set, n_set):
    """Find this."""
    set_one = {input() for _ in range(m_set)}
    set_two = {input() for _ in range(n_set)}
    set_both = set_one.intersection(set_two)
    set_both = sorted(set_both, reverse=True)
    if len(set_both) != 0:
        for i in set_both:
            print(i)
    else:
        print("Nope ")

sets(int(input()), int(input()))
