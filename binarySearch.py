lists=[]

n=int(input("Enter the value of n: "))
for i in range(n):
    num=int(input(f"Enter the num {i}: "))
    lists.append(num)

lists.sort()
print("Sorted list:", lists)

low=0
high=len(lists)-1
key=int(input("Enter the value to be found: "))

def binarySearch(nums,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2

    if nums[mid]==key:
        return mid
    elif nums[mid]>key:
        return binarySearch(nums,low,mid-1,key)
    else:
        return binarySearch(nums,mid+1,high,key)


value=binarySearch(lists,0,n-1,key)
if value!=-1:
    print(f"{key} is found at index: {value}")
else:
    print(f"{key} not found!")
