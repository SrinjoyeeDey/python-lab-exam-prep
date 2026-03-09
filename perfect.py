num=int(input("Enter the number: "))

sums=0
for i in range(1,num):
    if num%i==0:
        sums+=i

if sums==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

# a number into words digit by digit (like 4053 → four zero five three)

num2=int(input("Enter the number: "))

words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

for digit in str(num2):
    print(words[int(digit)],end=" ")