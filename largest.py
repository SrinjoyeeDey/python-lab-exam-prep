list=[]

n=int(input("Enter the value of n: "))
for i in range(n):
    num=int(input(f"Enter the num {i}: "))
    list.append(num)

largest=0
second_largest=0

for i in list:
    if i>largest:
        largest=i

for i in list:
    if i>second_largest:
        if i != largest:
            second_largest=i

print(f"The largest number is: {largest}")
print(f"The second largest number is: {second_largest}")