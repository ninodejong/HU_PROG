bestand = (open("/home/nino/dev/HU/kluizen.txt", "r"))

def toon_aantal_kluizen_vrij():
    lines = bestand.readlines()
    linecount = sum(1 for line in lines)
    vrijkluis = (12-linecount)
    return (vrijkluis)

def nieuwe_kluis():
    lines = bestand.readlines()
    kluisvol = toon_aantal_kluizen_vrij()
    if kluisvol < 1:
        return("Geen Kluizen Beschikbaar")
    else:
        bestand.close()
        file = open('/home/nino/dev/HU/kluizen.txt', 'a+')
        code = int(input('Uw beveiligings code : '))
        nwe_kluisnummer = len(lines) + 2
        file.writelines(str(nwe_kluisnummer)+", "+str(code)+'\n')
        return ('Uw kluisnummer is: '+str(nwe_kluisnummer)+" Met de door u gekozen code")
        file.close()

def kluis_openen():
    nummer = input("Wat is je kluisnummer?")
    code = input("Wat is je code?")
    lines = bestand.readlines()
    for regel in lines:
        kluisinfo = regel.split(",")
        kluisnummer = kluisinfo[0]
        kluiscode = kluisinfo[1].strip()
        if nummer == kluisnummer:
            if code == kluiscode:
                return ("Kluis Geopend")
            else:
                return ("Code/Nummer Incorrect")
        else:
            return ("Code/Nummer Incorrect")

print('Maak een keuze uit de onderstaande opties:')
print('1: Ik wil weten hoeveel kluizen nog vrij zijn ')
print('2: Ik wil een nieuwe kluis ')
print('3: Ik wil even iets uit mijn kluis halen ')

user_input = int(input('Keuze: '))
if user_input == 1:
    print(toon_aantal_kluizen_vrij())
elif user_input == 2:
    print(nieuwe_kluis())
elif user_input == 3:
    print(kluis_openen())
else:
    print('Maak alleen de keuze uit de boven staande punten')

bestand.close()