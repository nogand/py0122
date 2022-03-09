factores=[2,3,5]
columnas=3

def divisores(num) :
    retorno=[]
    for i in factores:
        if num % i == 0 :
            retorno.append(i)
    if len(retorno) == 0 :
        return ""
    else :
        return " "+str(tuple(retorno)).replace(",)",")")

for i in range(1,101):
    if (i % columnas) == 0 :
        print(str(i)+divisores(i))
    else :
        print("{0: <25}".format(str(i)+divisores(i)),end="")
