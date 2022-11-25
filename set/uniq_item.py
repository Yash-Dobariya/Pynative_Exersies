# Get Only unique items from two sets


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set(set1|set2)

print(set3)