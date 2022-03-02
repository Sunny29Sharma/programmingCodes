def checkIsPrime(n):
    isPrime = True
    for i in range(2,n):
        if(n%i==0):
            isPrime = False
            break
    return isPrime




n  = int(input("Enter any number : "))
if(checkIsPrime(n)):
    print("yes")
else:
    print("no")