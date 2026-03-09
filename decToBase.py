def decimal_to_base(num,base):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if num==0:
        return "0"
    res=""

    while num>0:
        remainder=num%base
        res=digits[remainder]+res
        num//=base

    return res

number = int(input("Enter decimal number: "))
base = int(input("Enter base (2-36): "))

converted= decimal_to_base(number,base)
print(converted)