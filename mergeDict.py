d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

d3={}
for k in d1:
    d3[k]=d1[k]

for k in d2:
    d3[k]=d2[k]

print(d3)
