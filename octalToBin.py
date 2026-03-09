num=int(input("Enter a decimal number: "))

octal=""

while num>0:
    remainder=num%8
    octal=str(remainder)+octal
    num//=8

print(f"Octal number is: {octal}")


# Octal to Binary

octal=input("Enter a octal number: ")
decimal=0
power=0

for digit in reversed(octal):
    decimal+=int(digit)*(8**power)
    power+=1

print("Decimal number:", decimal)