"""Crewmate"""


def imposter():
    """Find this."""
    alive = {}
    dead = {}
    imp = 0
    start = False
    while True:
        person = input()
        if person == "End":
            break
        elif person == "Start":
            start = True
        elif start == True:
            vote = alive.pop(person)
            dead[person] = vote
        else:
            person = [tuple(person.strip('{}""').split('" : "'))]
            alive.update(person)
    for i in alive.values():
        if i == "Impostor":
            imp += 1

    dead = dict(sorted(dead.items(), key=lambda rip: rip[0]))
    alive = dict(sorted(alive.items(), key=lambda rip: rip[0]))

    print(imp, "Impostor Remains")
    print("***Alive***")
    for key, value in alive.items():
        print(key, ":", value)
    print("***Dead***")
    for key, value in dead.items():
        print(key, ":", value)

imposter()
