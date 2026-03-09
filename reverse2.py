num=int(input("Enter a number to reverse: "))

reverse=0;
temp=num

while(temp>0):
    digit=temp%10
    reverse=reverse*10 + digit
    temp//=10

print(f"The reverse number is: {reverse}")