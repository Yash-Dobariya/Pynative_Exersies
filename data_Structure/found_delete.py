# Checks if one set is a subset or superset of another set. If found, delete all elements from that set


first_data_set = {27, 43, 34}
secound_data_set = {34, 93, 22, 27, 43, 53, 48}

data_set=first_data_set.issubset(secound_data_set)
print("first_data_set is subset of secound_data_set =",data_set)

data_set1=secound_data_set.issubset(first_data_set)
print("secound_data_set is sub set of a first_data_set = ",data_set1)

print("\n")

data_set2 =first_data_set.issuperset(secound_data_set)
print("first_data_set is superset of secound_data_set =",data_set)

data_set1=secound_data_set.issuperset(first_data_set)
print("secound_data_set is super set of a first_data_set = ",data_set1)

print("\n")

print("//clear all element of a set//")

first_data_set.clear()
print(first_data_set)
print(secound_data_set)