list=[]

n=int(input("Enter the value of n: "))
for i in range(n):
    num=int(input(f"Enter the num {i}: "))
    list.append(num)

left=0
right=len(list)-1

while(left<right):
    list[left],list[right]=list[right],list[left]
    left+=1
    right-=1

print(list)
