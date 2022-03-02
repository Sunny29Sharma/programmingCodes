mylist1=[10,20,30,40,50]
n = int(input())
count = 0
for i in mylist1:
    if(i == n):
        count+=1

print(f"{n} appeared {count} time")
