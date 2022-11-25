"""Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5"""

row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
        print("")

# row = 5

# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")
      
