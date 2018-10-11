def ticker(filename):
    file = open(filename, "r")
    return file.read()

f = ticker('filedixt.txt').split(':')
print(f.strip())