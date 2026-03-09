s=input("Enter a word/sentence: ")
res=""
for ch in s:
    if ch>='A' and ch<='Z':
        res+=chr(ord(ch)+32)
    elif ch>='a' and ch<='z':
        res+=chr(ord(ch)-32)
    else:
        res+=ch

print(f"Comverted string: {res}")