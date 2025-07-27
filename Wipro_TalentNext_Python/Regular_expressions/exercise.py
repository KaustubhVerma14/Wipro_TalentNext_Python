# Q) Write a program to find check if a string has only octal digits. Given string ['789','123','004'].

'''def is_octal(s):
    for i in s:
        if i not in '01234567':
            return False
    return True
strings=['789','123','004']
for i in strings:
    if is_octal(i):
        print(i,'only has octal digits')
    else:
        print(i,'also has non octal digits')'''


# Q) Extract the user id, domain name and suffix from the following email addresses. emails=["zuck@facebook.com",
#    "sunder33@google.com","jeff42@amazon.com"]

'''import re
emails = ["zuck@facebook.com", "sunder33@google.com", "jeff42@amazon.com"]

pattern = r"([\w\d]+)@([\w\d]+)\.([a-z]+)"

for i in emails:
    match = re.match(pattern, i)
    if match:
        user_id, domain, suffix = match.groups()
        print(f"Email: {i}")
        print(f"  User ID  : {user_id}")
        print(f"  Domain   : {domain}")
        print(f"  Suffix   : {suffix}")
        print()'''


# Q) Split the following irregular sentence into proper words. sentence="""A, very     very; irregular_sentence"""

'''import re
sentence = """A, very     very; irregular_sentence"""
words = re.sub(r'[^\w]', ' ', sentence).split()
res=" "
for i in words:
    res=res+i+" "
print(res)'''


# Q) Clean up the following tweet.

"""import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'RT\s@\w+:', '', tweet)
tweet = re.sub(r'cc:\s@\w+', '', tweet)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'[^\w\s]', '', tweet)
tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)"""


# Q) Identify the words that start and end with the same letter.

l1=['civic','trust','widows','maximum','museums','aa','as']
for i in l1:
    if i[0]==i[-1]:
        print(i,end=" ")
    