def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def tabel():
    x = ' '
    print(3*x+'F'+6*x+'C')
    for i in range(-30, 50, 10):
        print('{:6}   {:2}'.format(convert(i), i))

print(tabel())