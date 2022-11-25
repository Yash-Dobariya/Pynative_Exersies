# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. 
# Only update the first occurrence of an item.


list1 = [5, 10, 15, 20, 25, 50, 20]

print("location of a value :")
find= list1.index(20)

print(find)

print("insert a value :")

change = list1.insert(find,200)
print(list1)
print("remove 20 :")
change1 = list1.remove(20)
print(list1)
