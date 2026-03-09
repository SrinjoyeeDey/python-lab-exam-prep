L = [3, 1, 4]
M = [1, 5, 9]

N=[]

for i in range(len(L)):
    N.append(L[i]+M[i])

print(N)

str_list = ["apple", "banana", "kiwi", "strawberry"]
max_len=len(str_list[0])

for i in str_list:
    if len(i)>max_len:
        max_len=len(i)

print(f"Maximum length is: {max_len}")

list2=[]

for i in range(1,27):
    ch=chr(96+i)
    list2.append(ch*i)

print(list2)