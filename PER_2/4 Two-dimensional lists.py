studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    average = []
    for i in studentencijfers:
        som = 0
        for x in i:
            som = som + x
        average.append(som / len(i))
    return average

def gemiddelde_van_alle_studenten(studentencijfers):
    average = []
    for i in studentencijfers:
        som = 0
        for x in i:
            som = som + x
        average.append(som / len(i))
    return (sum(average)/len(average))

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))