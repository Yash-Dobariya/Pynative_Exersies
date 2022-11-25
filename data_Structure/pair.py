# Create a Python set such that it shows the element from both lists in a pair


data_list1 = [2, 3, 4, 5, 6, 7, 8]
data_list2= [4, 9, 16, 25, 36, 49, 64]


data_list3=set(zip(data_list1,data_list2))
print(data_list3)