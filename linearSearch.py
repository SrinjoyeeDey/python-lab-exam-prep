lists=[]

n=int(input("Enter the value of n: "))
for i in range(n):
    num=int(input(f"Enter the num {i}: "))
    lists.append(num)

key=int(input("Enter the key: "))

def linearSearch(lists,key):
    for i in range(len(lists)):
        if lists[i]==key:
            return i
    return -1

value=linearSearch(lists,key)

if value!=-1:
    print(f"The {key} is found at index {value}")
else:
    print(f"The {key} is not found")

