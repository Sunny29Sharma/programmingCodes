for i in range(10,100):
    prime = True
    for j in range(2,i):
        if(i%j == 0):
            prime = False
            break
    if(prime):
        print(i)
