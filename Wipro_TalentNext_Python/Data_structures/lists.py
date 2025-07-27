# Q) Write a program to create a list of 5 integers and display the list items. Access individual elements
#    through index.

'''l1=[]
while len(l1)<5:
    a=int(input("enter a number: "))
    l1.append(a)
print("The list is",l1)
index=int(input("enter a number from 0-4: "))
print(l1[index])'''


# Q) Write a program to append a new item to the end of a list.

'''l2=[1,2,3,4,5]
l2.append(6)
print(l2)'''


# Q) Write a program to reverse the order of the items in the list.

'''l2=[1,2,3,4,5]
print(l2[::-1])'''


# Q) Write a program to print the number of occurences of a specific item in a list.

'''l3=[1,1,2,3,1,4,5]
count=0
for i in l3:
    if i==1:
        count+=1
print(count)'''


# Q) Write a program to append the items of list1 to list2 in the front.

'''list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)'''


# Q) Write a program to insert a new item before the second element in an existing list.

'''l2=[1,2,3,4,5]
a=6
l2.insert(1,a)
print(l2)'''

# Q) Write a program to remove the item from a specified index from the list.

'''l2=[1,2,3,4,5]
a=int(input("enter the index value from 0-4 from which element is to be removed: "))
l2.pop(a)
print(l2)'''


# Q) Write a program to remove the first occurence of a specified element from a list.

l3=[1,1,2,2,3,1,3,4,5]
l3.remove(3)
print(l3)