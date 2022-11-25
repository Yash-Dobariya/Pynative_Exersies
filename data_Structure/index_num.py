# Create a list by picking an odd-index items from the first list and even index items from the second


data_list_1 = [3, 6, 9, 12, 15, 18, 21]
data_list_2 = [4, 8, 12, 16, 20, 24, 28]

data_list_3=[]

odd_list=data_list_1[1::2]

even_list=data_list_2[0::2]

data_list_3.extend(odd_list)
data_list_3.extend(even_list)

print(data_list_3)
