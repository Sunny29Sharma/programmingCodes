from sys import argv


def checkPrime(n):
    isPrime = True
    for i in range(2,n):
        if(n%i==0):
            isPrime = False
            break
    return isPrime

sum = 0
for i in range(1,11):
    if(checkPrime(argv[i])):
        sum += argv[i]
print(sum)
