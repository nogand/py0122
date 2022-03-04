for i in range(1,101):
    print(i,end="")
    divisores=[]
    if i % 2 == 0:
        divisores.append(2)
    if i % 3 == 0:
        divisores.append(3)
    if i % 5 == 0:
        divisores.append(5)
    if len(divisores) == 0 :
        divisores = ""
    else :
        divisores=" "+str(tuple(divisores)).replace(",)",")")
    print(divisores)
