# Q) Write a program to read the entire content from a txt file and display it to the user.

'''filename=input("Enter the filename: ")
file = open(filename, 'r')
content = file.read()
print("\n--- File Content ---\n")
print(content)
file.close()'''


# Q) Write a program to read the first n lines from the txt file. Get n as user input.

'''filename = input("Enter the filename: ")
n = int(input("Enter how many lines to read: "))
file = open(filename, 'r')
for i in range(n):
    line = file.readline()
    if line == '':
        break  
    print(line.strip())
file.close()'''


# Q) Write a program to accept input from user and append it to a txt file.

'''filename = input("Enter the filename (with .txt extension): ")
text = input("Enter the text to append: ")
file = open(filename, 'a')
file.write(text + '\n')
file.close()
print("Text appended successfully.")'''


# Q) Write a program to read txt contents from a txt file line by line and store each line into a list.

'''filename = input("Enter the filename: ")
file = open(filename, 'r')
lines = file.readlines()
file.close()
lines = [line.strip() for line in lines]
print("Contents of the file as a list:")
print(lines)'''


# Q) Write a program to find the longest word from the txt file contents, assuming that the file will have only 
#    one longest word in it.

'''filename = input("Enter the filename (with .txt extension): ")
file = open(filename, 'r')
text = file.read()
file.close()
words = text.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)'''


# Q) Write a program to count the frequency of a user entered word in a txt file.

filename = input("Enter the filename (with .txt extension): ")
search_word = input("Enter the word to count: ")
file = open(filename, 'r')
text = file.read()
file.close()
words = text.split()
count = sum(1 for word in words if word.lower() == search_word.lower())
print(f"The word '{search_word}' appears {count} times in the file.")