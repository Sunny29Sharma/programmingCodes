def checkForPrime(n):
    prime = True
    for i in range(2,n):
        if(n%i == 0):
            prime = False
            break
    if(prime):
        print("Number is Prime")
    else:
        print("Number is not Prime")
            


n = int(input("Enter the number : "))
checkForPrime(n)
