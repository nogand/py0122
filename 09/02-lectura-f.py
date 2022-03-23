filename="/etc/passwd"
k=1

with open(filename, 'r') as fp:
    for line in fp:
        print(f'{str(k).zfill(3):5}{line[:35]}'.rstrip("\n"))
        k+=1
