num=int(input("Enter the number: "))
temp=num
sums=0

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

while temp>0:
    digit=temp%10
    sums+=fact(digit)
    temp//=10

if sums==num:
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
