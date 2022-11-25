db_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]


# for i in db_list:
# print(' '.count())



count_dict=dict()
for item in db_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)
