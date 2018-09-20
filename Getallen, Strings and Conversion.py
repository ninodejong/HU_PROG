cijferICOR = float(6.0)
cijferPROG = float(8.5)
cijferCSN = float(7.0)

calcGrade = ((cijferCSN + cijferICOR + cijferPROG) / 3)
averageGrade = round(calcGrade,2)
pay = averageGrade * 30

print("Mijn cijfers gemiddeld een ",averageGrade," leveren een beloning van €",pay,"pop!")