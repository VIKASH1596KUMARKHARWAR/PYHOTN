l = [1,2,3,4,5,6,7]

l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
print(l1)


l2 =["sudha","megha","ghf"]
l3=[]
for i in l2:
    print(i.upper()) 
    l3.append(i.upper())
print(l3)
print(f"The contents of the list l3 are as follows: {l3}")
print("The contents of the list l3 are as follows: " + str(l3))

