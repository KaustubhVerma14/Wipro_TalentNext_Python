# Q) Write a program to add a key and value to a dictionary.

'''dict1= {0:10, 1:20}
dict1[2]=30
print(dict1)'''


# Q) Write a program to concatenate the following dictionaries.

'''dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
res=dict1|dict2|dict3
print(res)'''


# Q) Write a program to check if a given key already exists in a dictionary.

"""dict1={1:10,2:20,3:30}
if 1 in dict1:
    print("yes")
else:
    print("no")"""


# Q) Write a program to iterate over a dictionary using a for loop and print the keys alone the values alone and
#    both keys and values.

'''dict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for i in dict1:
    print(i)
for i in dict1:
    print(dict1[i])
for i in dict1:
    print(i,dict1[i])'''


# Q) Write a program to prepare a dictionary where the keys are numbers between 1 and 15 and the valuesz are the
#    squares of the keys.

'''for i in range(1,16):
    print(i,":",i**2,end=", ")'''


# Q) Write a program to sum all the values in a dictionary, considering the values will be of int type.

dict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum=0
for i in dict1:
    sum+=dict1[i]
print(sum)