# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

sort=(sorted(str(tuple1), key=lambda x: x[1]))
print(sort)