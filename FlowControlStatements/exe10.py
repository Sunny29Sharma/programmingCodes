def checkPalindrom(n):
    ans = 0
    n1 = n
    while(n>0):
        val = n%10
        ans = ans*10 + val
        n = n//10
    #print(ans)
    if(ans == n1):
        return True
    return False


n = int(input("Enter any Number : "))
if(checkPalindrom(n)):
    print(f"{n} is palindrom")
else:
    print(f"{n} is not palindrom")
