s = input("Enter fileName : ")
try:
    f = open(s,'r')
    print(f.read())

except:
    print("file not exist")