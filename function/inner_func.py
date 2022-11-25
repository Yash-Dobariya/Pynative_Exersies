#  Create an inner function to calculate the addition in the following way

# 1. Create an outer function that will accept two parameters, a and b
# 2. Create an inner function inside an outer function that will calculate the addition of a and b
# 3. At last, an outer function will add 5 into addition and return it


def outer_fun(a, b):
    
    def addition(a, b):
        return a + b

   
    add = addition(a, b)
  
    return add + 5

result = outer_fun(5, 10)
print(result)