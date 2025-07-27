# Q) Write a function to return the sum of all numbers in a list.

'''def sum(l1):
    sum=0
    for i in l1:
        sum+=i
    return sum
a=[8,2,3,0,7]
print(sum(a))'''


# Q) Write a function to return the reverse of a string.

'''def reverse_string(a):
    return a[::-1]
a='1234abcd'
print(reverse_string(a))'''


# Q) Write a function to calculate and return the factorial of a number.

'''def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    res=1
    for i in range(1,n+1):
        res*=i
    return res
print(factorial(6))'''


# Q) Write a function that accepts a string and prints the number of upper case and lower case letters in it.

'''def count(a):
    upper_case=0
    lower_case=0
    for i in a:
        if ord(i)>95:
            lower_case+=1
        elif ord(i)>64 and ord(i)<92:
            upper_case+=1
        else:
            pass
    return upper_case,lower_case
a="Wipro Talent Next"
print(count(a))'''


# Q) Write a function to print the even numbers from a given list. List is passed to the function as an argument.

'''def even_numbers(l1):
    for i in l1:
        if i%2==0:
            pass
        else:
            l1.remove(i)
    return l1
print(even_numbers([1,2,3,4,5,6,7,8,9]))'''


# Q) Write a function that takes a number as a parameter and checks whether it si prime or not.

def prime(n):
    count=0
    if n==1:
        return n,'is not a prime number'
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                count+=1
            else:
                pass
    if count==0:
        return n,'is a prime number'
    else:
        return n,'is not a prime number'
print(prime(7))