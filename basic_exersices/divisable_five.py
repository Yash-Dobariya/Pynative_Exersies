# Iterate the given list of numbers and print only those numbers which are divisible by 5

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)
