"""Kabata"""
def main():
    """maiin"""
    keyword = ["bakka", "ka", "ba", "ta"]
    for _ in range(int(input())):
        txt = input().replace("baka", "No")
        for i in keyword:
            txt = txt.replace(i, "")
        print("yes" if txt.strip() == "" else "no")
main()
