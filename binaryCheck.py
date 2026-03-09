num=input("Enter a number: ")

binary=True
for i in num:
    if i!='0' and i!='1':
        binary=False
        break

if binary:
    print(f"{num} is binary")
    print("Odd position characters are: ")
    for i in range(0,len(num),2):
        print(num[i],end="")
else:
    print(f"{num} is not binary")