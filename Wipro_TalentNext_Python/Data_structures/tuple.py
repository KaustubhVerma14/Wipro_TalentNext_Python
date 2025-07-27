# Q) Write a program to find the 4th element from the first and 4th element from the last in a tuple.

'''tpl1=(1,2,3,4,5,6,7,8,9,0)
print(tpl1[3])
print(tpl1[-4])'''


# Q) Write a program to check whether an element exists in a tuple or not.

'''tpl1=(1,2,3,4,5,6,7,8,9,0)
if 5 in tpl1:
    print("yes")
else:
    print("no")'''


# Q) Write a program to convert a list into a tuple.

'''l1=[1,2,3,4,5,6,7,8,9,0]
tpl1=tuple(l1)
print(tpl1)'''


# Q) Write a program to find the index of an item in a tuple.

'''tpl1=(1,2,3,4,5,6,7,8,9,0)
print(tpl1.index(4))'''


# Q) Write a program to replace the last value of tuples in a list to 100.

l1=[(1,2,3),(4,5,6),(7,8,9)]
for i in range(len(l1)):
    l1[i]=l1[i][:-1]+(100,)
print(l1)