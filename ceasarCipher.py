text=input("Enter the sentence: ")
shift=int(input("Enter the shift number: "))

result=""
for ch in text:
    if ch.isalpha():
        new_char=chr((ord(ch)-ord('a')+shift)%26+ord('a'))
        result+=new_char
    else:
        result+=ch
print(f"Encrypted message: {result}")

result2=""
for ch in result:
    if ch.isalpha():
        new_char=chr((ord(ch)-ord('a')-shift)%26+ord('a'))
        result2+=new_char
    else:
        result2+=ch
print(f"Decrypted message: {result2}")