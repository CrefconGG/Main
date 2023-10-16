"""AndAgain"""


def aeiou():
    """Find this."""
    count = 0
    have = 0
    abc = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    ans = []
    word = input().replace(".", "")
    ans.extend(word.split(" "))
    ans.sort()
    for i in ans:
        count = 0
        for j in i:
            if j in abc and len(i) >= 2:
                count += 1
                if count == 2:
                    print(i)
                    have += 1
                    break
    if have == 0:
        print("Nope")



aeiou()
