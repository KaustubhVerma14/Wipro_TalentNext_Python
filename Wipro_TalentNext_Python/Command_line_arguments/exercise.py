# Q) Write a program to accept 2 numbers as command line arguments and display their sum.

a=int(input("enter a number: "))
b=int(input("enter another number: "))
sum=a+b
print(sum)

# Q) Write a program to accept a welcome message through command line arguments and display the file name along 
#    with the welcome message.

import sys 
print("Welcome", sys.argv[0])

# Q) Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers 
#    among them.

l1=[]
sum=0
while len(l1)<10:
    a=int(input("enter a number:"))
    l1.append(a)
for i in l1:
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0 and i>1:
        sum+=i
print(sum)
