# Q) Write a program to check if a given number is positive, negative or 0.

'''a=int(input("enter a number: "))
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,'is a negative number')
else:
    print("The number given is 0")'''


# Q) Write a program to check if a given number is odd or even.

'''num=int(input("enter a number: "))
if num%2==0:
    print(num,'is an even number')
else:
    print(num,'is an odd number')'''


# Given two non negative values, print true if the have the same last digit such as 27 and 57.

'''num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
num1=str(num1)
num2=str(num2)
if num1[-1]==num2[-1]:
    print("True")
else:
    print("False")'''


# Q) Write a program to print numbers from 1 to 10 in a single row with one tab space.

'''for i in range(1,11):
    print(i,end=" ")'''


# Q) Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

'''for i in range(23,57):
    if i%2==0:
        print(i)'''


# Q) Write a program to check if a given number is prime or not.

'''num=int(input("enter a number: "))
count=0
if num==1:
    print(num,'is not a prime number')
else:
    for i in range(2,num//2+1):
        if num%i==0:
            count+=1
        else:
            pass
    if count==0:
        print(num,'is a prime number')
    else:
        print(num,'is not a prime number')'''


# Q) Write a program to print prime numbers between 10 and 99.

'''for i in range(10,100):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i,end=" ")'''


# Q) Write a program to print the sum of all the digits of a given number.

'''a=1234
sum=0
temp=a
while temp>0:
    x=temp%10
    sum+=x
    temp//=10
print(sum)'''


# Q) Write a program to reverse a given number and print.

'''a=int(input("enter a number: "))
a=str(a)
print(a[::-1])'''


# Q) Write a program to find if a given number is pallindrome or not.

a=int(input("enter a number: "))
a=str(a)
if a==a[::-1]:
    print(a,'is pallindrome')
else:
    print(a,'is not pallindrome')