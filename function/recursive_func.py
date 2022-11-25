# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10

def addition(num):
    if num:
         return num + addition(num - 1)
    else:
        return 0
res = addition(999)
print(res)