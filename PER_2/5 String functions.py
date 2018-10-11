zin = input("Typ een willekeurige zin in: ")
def gemiddelde(string):
    char = 0
    list1 = [string]
    spllist1 = [i.split(' ') for i in list1]
    spllist2 = spllist1[0]
    wordcount = len(spllist2)
    for i in string:
        char = char+1
        if(i == ' '):
            char = char-1
    return (char/wordcount)
print(gemiddelde(zin))