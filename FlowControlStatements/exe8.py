def sumOfDigits(n):
    res = 0
    while(n>0):
        n1 = n%10
        res = res + n1
        n = n//10
    return res




n = int(input("Enter the number : "))
print(sumOfDigits(n))
