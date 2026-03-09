# num=int(input("Enter a number for palindrome number check: "))

# reverse=0
# temp=num

# while(temp>0):
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp//=10

# if reverse==num:
#     print(f"{num} is a palindrome number")
# else:
#     print(f"{num} is not a palindrome number")


string=input("Enter a string for palindrome number check: ")

palindrome=True
n=len(string)

for i in range(n//2):
    if string[i]!=string[n-i-1]:
        palindrome=False
        break

if palindrome:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
