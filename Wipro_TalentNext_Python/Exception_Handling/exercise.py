# Q) Write a program to accept two numbers from the user and perform division. If any exception occurs, print an 
#    error message or print the results.

'''try:
    num1=int(input("enter a number: "))
    num2=int(input("enter another number: "))
    res=num1/num2
    print('result is:',res)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("enter valid numbers")
except Exception as e:
    print("some error occured")'''


# Q) Write a prograam to accept a number from the user and check whether its prime or not. If user enters anything
#    other than a number, handle the exception and print an error message.

'''try:
    num=int(input("enter a number: "))
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
            print(num,'is not a prime number')
except ValueError:
    print("enter a valid number")
except Exception as e:
    print("an error occured")'''


# Q) Write a program to accept the file name to be opened from the user, if file exists print the contents of the
#    file in title case or handle the exception and print an error message.

'''try:
    file_name=input("Enter the file name: ")
    with open(file_name, 'r') as file:
        content=file.read()
    print("File content in title case:")
    print(content.title())
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An error occurred:")'''


# Q) Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is 
#    positive or negative number. If any invalid index is entered, handle the exception and print an error message.

l1=[12, -7, 5, -3, 9, -1, 0, 4, -6, 8]
try:
    index=int(input("enter the index value from 0 to 9: "))
    if l1[index]>0:
        print("the number at index",index,'is positive')
    elif l1[index]<0:
        print('the number at index',index,'is negative')
    else:
        print("the number at index",index,'is zero')
except ValueError:
    print("enter a valid number in the list")
except IndexError:
    print("enter a valid index value between 0 and 9")