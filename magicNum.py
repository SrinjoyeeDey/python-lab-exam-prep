n=int(input("Enter the number: "))
num=n
while n>9:
    s=0
    while n>0:
        digit=n%10
        s+=digit
        n//=10
    n=s

if n==1:
    print(f"{num} is a Magic Number")
else :
    print(f"{num} is not a Magic Number")