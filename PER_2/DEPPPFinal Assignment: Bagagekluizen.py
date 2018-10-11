def option_menu():
    options = [['1','Ik wil weten hoeveel kluizen nog vrij zijn','free_space'],['2','Ik wil een nieuwe kluis','new_space'],['3','Ik wil even iets uit mijn kluis halen','kluis_openen'],['4','Ik geef mijn kluis terug','delete_space']]
    return options
def user_input():
    options = option_menu()
    option_pos = []
    for o in options:
        option_pos.append(o[0])
    print('Maak een keuze uit de onderstaande opties:')
    for option in options:
        print(option[0]+': '+option[1]+'.')
    user_input = input('Keuze: ')
    user_key = user_input
    user_input = int(user_input) - 1
    if user_key in option_pos:
        exec(options[int(user_input)][2]+'()')
    else:
        print('Maak alleen de keuze uit de boven staande punten')

def kluis_openen():
    file = open("/home/nino/dev/HU/kluizen.txt", "r")
    safe_num = int(input("Wat is je kluisnummer?"))
    safe_pass = int(input("Wat is je code?"))
    lines = file.readlines()
    file.close()
    for line in lines:
        safe_info = line.split(',')
        safe_numbers = safe_info[0]
        safe_passes = safe_info[1].split()
        # print(safe_passes)
        if safe_num == safe_numbers:
            if safe_pass == int(safe_passes):
                 return ("Kluis Geopend")
            else:
                 return ("Code/Nummer Incorrect")
        else:
            return ("Code/Nummer Incorrect")


user_input()