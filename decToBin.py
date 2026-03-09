# Decimal to Binary
number = int(input("Enter decimal number: "))

binary=""
while number>0:
    rem=number%2
    binary=str(rem)+binary
    number//=2

print("Binary =", binary)

# Binary to Decimal

binary = input("Enter binary number: ")

decimal=0
power=0

for digit in reversed(binary):
    decimal+=int(digit)*(2**power)
    power+=1

print("Decimal =", decimal)
