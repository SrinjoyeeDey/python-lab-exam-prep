# Prime Numbers that can be expressed as the sum of other prime numbers
def isPrime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    
def primeSum(limit):
    primes=[]
    for i in range(2,limit+1):
        if isPrime(i):
            primes.append(i)
    s=0
    for i in range(len(primes)):
        s+=primes[i]
        if isPrime(s) and s<=limit:
            print(s)

n = int(input("Enter the limit: "))
primeSum(n)