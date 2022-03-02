mylist1 = [10,30,40,10,30]

element = 10
for i in mylist1:
    if element == i:
        mylist1.remove(i)
        break
print(mylist1)