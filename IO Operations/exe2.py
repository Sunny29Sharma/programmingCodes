n = int(input("Enter number : "))
f = open("file.txt",'r')
for i in range(0,n):
    print(f.readline())