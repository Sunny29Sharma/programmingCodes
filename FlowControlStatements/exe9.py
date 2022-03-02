def getReverse(n):
    ans = 0
    while(n>0):
        val = n%10
        ans = ans*10 + val
        n = n//10
    print(ans)



n = int(input("Enter the number : "))
getReverse(n)
