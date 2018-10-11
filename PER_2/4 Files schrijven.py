import datetime

def today():
    today = datetime.datetime.today()
    output = today.strftime("%a %d %b %Y, %H:%M:%S")
    return output

while True:
    txt = '/home/nino/dev/HU/hardlopers.txt'
    file = open(txt,'a+')
    naam = str(input('Naam hardloper : '))
    file.writelines(today()+", "+naam+'\n')
    print('Writing: '+today()+", "+naam+' To file: '+txt)