myList1 = [10,20,30,40,50,60]

i = 0
j = len(myList1)-1
while(i < j):
    temp = myList1[i]
    myList1[i] = myList1[j]
    myList1[j] = temp
    i = i+1
    j = j-1

print(myList1)

