# Write a program to create function func1() to accept a variable length of arguments and print their value.

def value(a,b,c):
    print(a,b,c,)
print("Printing values:","\n",20,40,60)

def value(a,b):
    print(a,b)
print("Printing values:","\n",80,100)


#secound method
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)
