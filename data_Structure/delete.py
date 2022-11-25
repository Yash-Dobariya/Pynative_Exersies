#  Iterate a given list and check if a given element exists as a key’s value in a dictionary.
#  If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

value_dict=sample_dict.values()

if value_dict != roll_number :
    update_list=roll_number.remove(value_dict)
    print(update_list)
else:
    print("all element are same")
