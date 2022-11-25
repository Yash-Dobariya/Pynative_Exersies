# Slice list into 3 equal chunks and reverse each chunk


database_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


"""first method"""
# Print first 3 element
database_list_1=database_list[0:3]
#Reversed 
database_list_1.reverse()
print(database_list_1)

database_list_2=database_list[3:6]
database_list_2.reverse()
print(database_list_2)

database_list_3=database_list[6:]
database_list_3.reverse()
print(database_list_3)

"""Secound mehod"""

slise_len = len(database_list)//3
for i in range(3):
    p=i+1
    next_part = ( p * slise_len)
    print(database_list[i*slise_len:next_part])
    a= database_list.reverse()
    print(a)


