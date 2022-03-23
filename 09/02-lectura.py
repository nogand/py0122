filename="/etc/passwd"
k=1

with open(filename, 'r') as fp:
    for line in fp:
        print("{0:03}  {1}".format(k,line[:35].rstrip("\n")))
        k+=1
