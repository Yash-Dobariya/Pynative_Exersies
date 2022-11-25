"""# Given a two Python list. Write a program to iterate both lists simultaneously and display items from 
 list1 in original order and items from list2 in reverse order."""



list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in list1:

    print(i,end='')
  
list2.reverse()

print(list2)

a = ''.join(i,list2)
print(a)
