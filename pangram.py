s=input("Enter a sentence/word for pangram check: ")

alphabet="abcdefghijklmnopqrstuvwxyz"

flag=True
for ch in alphabet:
    if ch not in s:
        flag=False
        break

if flag:
    print(f"{s} is a pangram")
else:
    print(f"{s} is not a pangram")