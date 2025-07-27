# MINI-PROJECT 

try:
    filename=input("enter the file name:")
    file=open(filename+'.txt','r')
    total_items=0
    free_items=0
    amount_to_pay=0
    discount=0
    for i in file:
        i=i.strip()
        if i=='':
            continue
        a=i.split()
        if a[0].lower()=='discount':
            discount=int(a[1])
        elif a[-1].lower()=='free':
            free_items+=1
        else:
            price=int(a[-1])
            amount_to_pay+=price
            total_items+=1
    file.close()

    print("No. of items purchased:",total_items)
    print("No. of free items:",free_items)
    print("Amount to pay:",amount_to_pay)
    print("Discount given:",discount)
    print("Final Amount Paid:",amount_to_pay-discount)

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("enter a valid value")
except Exception as e:
    print("An error occured")