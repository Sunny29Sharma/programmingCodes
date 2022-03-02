myList1 = [10,20,30,40,50]
myList2 = [11,21]

myList2.extend(myList1)
myList1 = myList2
print(myList1)