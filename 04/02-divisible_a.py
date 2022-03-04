for i in range(1,101):
    print(i,"(",end="")
    if i % 2 == 0:
        print(2,",",end="")
    if i % 3 == 0:
        print(3,",",end="")
    if i % 5 == 0:
        print(5,",",end="")
    print(")")
