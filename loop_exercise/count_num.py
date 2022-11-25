# Write a program to count the total number of digits in a number using a while loop.


count_num = 75869
counter = 0

while count_num != 0:
    count_num = count_num // 10
    counter = counter + 1
    
print(counter)