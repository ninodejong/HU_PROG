input = "5-9-7-1-7-8-3-2-4-8-7-9"
sumlist = []

list = [i.split('-')[0] for i in input]
numlist = [x for x in list if x]
numlist.sort()

for i in numlist:
    sumlist.append(int(i))

print('Gesorteerde list van ints:'+str(numlist))
print('Grootste getal: '+max(numlist)+' en Kleinste getal: '+min(numlist))
print('Aantal getallen: '+str(len(numlist))+' en Som van de getallen: '+str(sum(sumlist)))
print('Gemiddelde: '+str(sum(sumlist)/len(sumlist)))
