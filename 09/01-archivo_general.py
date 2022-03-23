filename="01-ejemplo.txt"
filedata="prueba123"
newdata="otra prueba"

with open(filename, 'r') as f:
    f.read()

with open(filename, 'w') as f:
    f.write(filedata)

with open(filename, 'a') as f:
    f.write('\n' + newdata)
