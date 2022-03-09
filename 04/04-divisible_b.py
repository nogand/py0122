numeros=range(1,101)
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

for i in numeros:
    if (i % columnas) == 0 :
        print("{0: >3}{1: <13}".format(i,divisores(i)))
    else :
        print("{0: >3}{1: <13}".format(i,divisores(i)),end="")
