#  Find the intersection (common) of two sets and remove those elements from the first set

data_set1 = {23, 42, 65, 57, 78, 83, 29}
data_set2 = {57, 83, 29, 67, 73, 43, 48}

print("commen element fromm data_set1 and data_set2")
interseptor =data_set1.intersection(data_set2)
print(interseptor)

print("Remove element from set1")
interseptor1 =data_set1.symmetric_difference(interseptor)
print(interseptor1)



