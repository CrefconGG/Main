"""CuteCat CuteFox"""


def cutecat():
    """Find this."""
    aliancat = {"Garfield": "Cat01", "Fubuki": "Fox01"}
    cat = 0
    fox = 0
    num = int(input())
    for _ in range(num):
        dicc = input().strip('{}')
        key, value = dicc.split(':')

        if '"' in key or '"' in value:
            dicc = {key.strip(' "'): value.strip(' "')}
        elif "'" in key or "'" in value:
            dicc = {key.strip(" '"): value.strip(" '")}
        if "Garfield" in dicc.keys():
            aliancat.pop("Garfield")
        elif "Fubuki" in dicc.keys():
            aliancat.pop("Fubuki")
        if "Cat01" in dicc.values() and aliancat.get("Garfield") == "Cat01":
            aliancat.pop("Garfield")
        elif "Fox01" in dicc.values() and aliancat.get("Fubuki") == "Fox01":
            aliancat.pop("Fubuki")

        aliancat.update(dicc)
    cat_fox = sorted(aliancat.items(), key=sort)
    cat_fox = {key: value for key, value in cat_fox}
    for i in cat_fox.values():
        if i[:3] == "Cat":
            cat += 1
        else:
            fox += 1
    print("Cat :", cat)
    print("Fox :", fox)
    for key, value in cat_fox.items():
        print('{0} : {1}'.format(key, value))

def sort(word):
    """Sorting this."""
    return word[1][0], int(word[1][3:])

cutecat()
