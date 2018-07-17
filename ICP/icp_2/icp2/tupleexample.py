mylist=('bhargavi','reddy','siddipeta')
list_len=[]
for i in range(0,len(mylist)):
    list_len.append(len(mylist[i]))
listfinal=[]
print(list_len)

tup_1=tuple(mylist)
tup_2=tuple(list_len)

for i in range(0,len(tup_1)):
    tuple_3 = (tup_2[i], tup_1[i])
    listfinal.append(tuple_3)
print(listfinal)
listfinal.sort()
print(listfinal)
a = len(listfinal)
print("longest one in the group is: " ,listfinal[a-1])