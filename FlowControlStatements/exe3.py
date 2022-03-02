




def output(a,b):
    if((a%10) == (b%10)):
        return True
    return False







n1,n2 = map(int,input("Enter two numbers : ").split())
if(output(n1,n2)):
    print("True")
else:
    print("False")
