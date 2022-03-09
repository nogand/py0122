numeros=[101, 103, 105, 107, 333, 443, 300, 301, 302, 777]
factores=[2,3,5]
columnas=4

def divisores(num) :
    retorno=[]
    for i in factores:
        if num % i == 0 :
            retorno.append(i)
    if len(retorno) == 0 :
        return ""
    else :
        return " "+str(tuple(retorno)).replace(",)",")")

i=1
for num in numeros:
    if (i % columnas) == 0 :
        print("{0: >3}{1: <13}".format(num,divisores(num)))
    else :
        print("{0: >3}{1: <13}".format(num,divisores(num)),end="")
    i += 1
if (i-1) % columnas != 0 :
    print()