s = input("Enter your content: ")
f = open("file.txt",'a')
f.write(s)
f = open("file.txt",'r')
print(f.read())
