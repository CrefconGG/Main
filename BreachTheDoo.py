"""BreachTheDoo"""
import re

def six():
    """Find this."""
    word = input()
    sixty = re.split("[^a-zA-Z]", word)
    sixty = [x for x in sixty if len(x) > 6]
    sixty = " ".join(sixty)
    print(sixty)

six()
