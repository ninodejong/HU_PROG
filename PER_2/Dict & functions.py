def namen():
    dictionary = {}
    while True:
        naam = str(input("Volgende naam: "))
        if naam == "":
            for x, y in dictionary.items():
                if y <= 1:
                    print('Er is '+str(y)+' student met de naam ' + x)
                else:
                    print('Er zijn '+str(y)+' studenten met de naam '+x)
            break
        else:
            if naam in dictionary.keys():
                aantal = dictionary[naam]
                dictionary[naam] = aantal + 1
            else:
                dictionary[naam] = 1
namen()