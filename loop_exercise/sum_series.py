# Find the sum of the series upto n terms

n = 5
start=2
a=0
for i in range(n):
    print(start, end="+")
    a += start
    
    start = start * 10 + 2
print("\nSum of above series is:", a)