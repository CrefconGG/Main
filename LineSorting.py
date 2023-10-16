'''line'''
def main(time):
    '''sorting'''
    list1 = []
    for i in range(time):
        name = input()
        list1.append(name)
    mae = sorted(list1, key=len)
    for i in mae:
        print(i)
main(int(input()))
