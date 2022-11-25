# Write a program to use for loop to print the following reverse number pattern


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()