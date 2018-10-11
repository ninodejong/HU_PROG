# example input ["boter","kaas","bier","pizza", thee","drop","koek","cola","boterham","stamppot"]
zin = eval(input("Geef een lijst met minimaal 10 strings:"))

list = []

for i in zin:
    if len(i) == 4:
        list.append(i)
print("De nieuw-gemaakte lijst met alle vier-letter strings is:%r" % list)