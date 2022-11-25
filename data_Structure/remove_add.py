# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.


data_list = [34, 54, 67, 89, 11, 43, 94]



element=data_list.pop(4)
print(data_list)

data_list.insert(2,element)
print(data_list)

data_list.append(element)
print(data_list)


