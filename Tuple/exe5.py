myList = [(10,20,40),(40,50,60),(70,80,90)]


t = list(myList[2])
t.append(100)
t = tuple(t)
myList = myList[:2]
myList.append(t)
print(myList)