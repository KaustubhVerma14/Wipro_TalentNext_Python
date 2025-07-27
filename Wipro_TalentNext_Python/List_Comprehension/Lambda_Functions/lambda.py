# Q) Cubes of every number in the given list. list1=[1,2,3,4,5,6,7,8,9]

l1=[1,2,3,4,5,6,7,8,9]
cubes=list(map(lambda x:x**3, l1))
print(cubes)