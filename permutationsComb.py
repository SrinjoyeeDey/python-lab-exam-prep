n = int(input("Enter n: "))
r = int(input("Enter r: "))

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def perm(n,r):
    return fact(n)//fact(n-r)

def comb(n,r):
    return fact(n)//(fact(r)*fact(n-r))

print(f"The permutation is: {perm(n,r)}")
print(f"The combination is: {comb(n,r)}")
    