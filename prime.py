num=int(input("Enter a number for prime number check: "))

flag=True

for i in range (2,num):
    if num%i==0:
        flag=False
        break
if num>1 and flag:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")