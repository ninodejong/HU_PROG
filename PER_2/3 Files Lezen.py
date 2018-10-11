infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
line = 0
num = len(regels)
grootste = max(regels).split(",")

for regel in regels:
    if str(grootste[0]) in regel:
        line += -1
    else:
        line += 1


print('Deze file telt '+str(num)+' regels')
print('Het grootste kaartnummer is: '+str(grootste[0]) +' en dat staat op regel '+str(line))