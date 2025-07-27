# Q) Write a program to count the number of upper and lower case letters in a string.

'''a="LNCT Bhopal"
upper_case=0
lower_case=0
for i in a:
    if ord(i)>95:
        lower_case+=1
    elif ord(i)<95 and ord(i)>64:
        upper_case+=1
    else:
        pass
print(upper_case)
print(lower_case)'''


# Q) Write a program to check if a string is pallindrome or not.

'''a="ekitike"
if a==a[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")'''


# Q) Given a string return a new string made of n copies of the first 2 chars of the original string where n is 
#    the length of the string. The string length will be>=2.

'''a="Wipro"
n=len(a)
chars=a[:2]
new_str=chars*n
print(new_str)'''


# Q) Given a string, if the first or last character is x, return the string without those x characters, else
#    return the string unchanged.

'''a="xHix"
if a[0]=='x' and a[-1]=='x':
    print(a[1:-1])
else:
    print(a)'''


# Q) Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
#    You may assume that n is in between 0 and the length of the string inclusive.

a="Wipro"
n=3
chars=a[-3:]
print(chars*n)