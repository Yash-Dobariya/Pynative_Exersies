#  Reverse a given integer number


give_num=76542
reverse_num =0

while give_num > 0:
        reminder = give_num % 10
        reverse_num=reminder + (reverse_num *10)
        give_num=give_num// 10

print(reverse_num)