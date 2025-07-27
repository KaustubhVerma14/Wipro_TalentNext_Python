# MINI-PROJECT 1

"""def sort_colors(a):
    l1=a.split('-')
    l1.sort()
    res=""
    for i in l1:
        res=res+i+'-'
    res=res[:-1]
    return res
print(sort_colors('green-red-yellow-black-white'))
print(sort_colors('PINK-BLUE-TAN-PURPLE'))"""


# MINI-PROJECT 2

def ispallindrome(name):
    if name==name[::-1]:
        return 'Pallindrome'
    else:
        return 'Not Pallindrome'

def count_the_vowels(name):
    count=0
    for i in name:
        if i in "aeiou":
            count+=1
    return count

def frequency_of_letters(name):
    freq={}
    for i in name:
        freq[i]=freq.get(i,0)+1
    return freq

print(ispallindrome('marcel bentok tanaka'))
print(count_the_vowels('marcel bentok tanaka'))
print(frequency_of_letters('marcel bentok tanaka'))