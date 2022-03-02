s = input("enter string : ")
if(s[0] == 'x'):
    s = s[1:]
if(s[len(s)-1] == 'x'):
    s = s[:len(s)-1]
print(s)