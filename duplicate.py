list=[1,2,2,3,4]

unique=[]
duplicate=[]
flag=True

for num in list:
    if num not in unique:
        unique.append(num)
    else:
        duplicate.append(num)

print(f"The list of unique elements is: {unique}")
print(f"The list of duplicate elements is: {duplicate}")