def standaardprijs(afstandKM):
    if afstandKM > 0:
        if afstandKM > 50:
            kosten = (15 + afstandKM*0.60)
        else:
            kosten = afstandKM*0.80
    else:
        kosten = 0
    return(kosten)

def ritprijs(leeftijd, weekendrit, afstandKM):
    kosten = standaardprijs(afstandKM)
    if leeftijd <= 12 or leeftijd >= 65:
        if weekendrit == "Ja":
            tarief = (kosten*0.70)
        if weekendrit == "Nee":
            tarief = (kosten*0.65)
        print('De prijs van de reis is €' + str(round((tarief),2)) + ' euro')
    else:
        if weekendrit == "Ja":
            tarief =(kosten*0.60)
        else:
            tarief = (kosten)
        print('De prijs van de reis is €' + str(round((tarief),2)) + ' euro')

leeftijd = int(input('Hoe oud ben je?: '))
weekendrit = input('Is het weekend?: ')
afstandKM = int(input('Hoeveel Kilometers reis je?: '))
ritprijs(leeftijd, weekendrit, afstandKM)