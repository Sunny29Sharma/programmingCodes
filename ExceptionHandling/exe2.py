def checkPrime(n):

    isPrime = True
    for i in range(2,n):
        if(n%i==0):
            isPrime = False
            break
    return isPrime


try:
    n = int(input("Enter any number : "))
    if (checkPrime(n)):
        print("yes")
    else:
        print("no")
except:
    print("Please enter nubmer")

