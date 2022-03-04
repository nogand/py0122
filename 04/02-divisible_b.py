for i in range(1,101):
    print(i,end="")
    divisores=" ("
    if i % 2 == 0:
        divisores += "2"
    if i % 3 == 0:
        if divisores == " (" :
            divisores += "3"
        else :
            divisores += ", 3"
    if i % 5 == 0:
        if divisores == " (" :
            divisores += "5"
        else :
            divisores += ", 5"
    if divisores == " (" :
        divisores = ""
    else :
        divisores += ")"
    print(divisores)
