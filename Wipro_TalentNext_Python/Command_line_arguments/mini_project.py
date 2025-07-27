a=input("enter the number with all digits separated by hyphons: ")
b=input("enter another number with all digits separated by hyphons: ")
c=input("enter the numbers given: ")
l1=[]
l2=[]
l3=[]
l1=a.split("-")
l2=b.split("-")
l3=c.split("-")
happiness=0
for i in l3:
    if i in l1:
        happiness+=1
    elif i in l2:
        happiness-=1
    else:
        happiness+=0
print(happiness)