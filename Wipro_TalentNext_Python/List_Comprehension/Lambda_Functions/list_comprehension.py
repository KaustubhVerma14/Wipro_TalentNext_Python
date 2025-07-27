# Q) Write a LC program to create an output dictionary which contains only the odd numbers that are present in the 
#    input list=[1,2,3,4,5,6,7] as keys and their cubes as values.

l1=[1,2,3,4,5,6,7]
output_dict={x:x**3 for x in l1 if x%2!=0}
print(output_dict)


# Q) Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.

d1 = {chr(i): i - 96 for i in range(97, 123)}
print(d1)
