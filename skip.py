sentence=input("Enter the sentence: ")

res=""
for i in range(0,len(sentence),2):
    if sentence[i]!=" ":
        res+=sentence[i]
print(res)