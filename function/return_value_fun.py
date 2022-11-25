# Return multiple values from a function

def calculation(a, b):
    add=a+b
    sub=a-b
    return add,sub

res = calculation(40, 10)
print(res)