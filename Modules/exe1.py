import math_module
v = True
while(v):
    print("Enter 1 to add")
    print("Enter 2 to sub")
    print("Enter 3 to mult")
    print("Enter 4 to divide")
    print("Enter 0 to exit")
    n = int(input("Enter choice : "))
    if(n == 0):
        val = False
        break
    else:
        a = int(input("Enter first value : "))
        b = int(input("Enter second value : "))
        if(n == 1):
            print(math_module.add(a,b))
        elif(n == 2):
            print(math_module.sub(a,b))
        elif(n == 3):
            print(math_module.mult(a,b))
        else:
            print(math_module.div(a,b))


