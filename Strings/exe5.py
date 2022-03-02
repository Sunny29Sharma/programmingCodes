s = input("Enter string")
n = int(input("Enter number"))

index = n-1
newS = s[index:]
S = ""
for i in range(n):
    S += newS
print(S)