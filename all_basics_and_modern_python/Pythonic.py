#MAke it simple, faster and easier to read

#-------> and comparision
a,b = 5,5

# bad
print('same') if a == 5 and b == 5 else print('different')

# best
print('same') if a==b==5 else print('different')   # Called 'chaining'

#-------> looping number of times
#1 bad
for i in [0,1,2,3,4,5]:
    print (i)

#1 best
for i in range(6):                                  #range used to create a list in python 2,  but now  range performs the same as irange(which followes iteration protocol and produce generator object that does not take up memory)
    print (i)

#-------> looping each value
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#2 bad
for index in range(len(fruits)):
    print (fruits[index])                   #'[]' is the hint that you're doing it wrong, it needs to check the hash values and stuff to reference and stuff

#2 best
for fruit in fruits:
    print(fruit)

#-------> looping each value backwords
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#2 bad
for index in range(len(fruits)-1,-1,-1):
    print (fruits[index])

#2 best
for fruit in reversed(fruits):
    print(fruit)

#-------> looping each value with indices
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#3 bad
for index in range(len(fruits)):
    print (f'{index} -> {fruits[index]}')

#3 best
for index,fruit in enumerate(fruits):
    print (f'{index} -> {fruit}')

#-------> looping multiple lists at once(note both list's lengths)
fruits = ['apples', 'bananas', 'grapes', 'tomatos']
vegetables = ['carrot', 'spinach', 'cucumber']

#4 bad
smaller_size = min(len(fruits), len(vegetables))
for index in range(smaller_size):
    print (f'{fruits[index]} -> {vegetables[index]}')       #more '[]''s means more slower

#4 best
for fruit,vegetable in zip(fruits,vegetables):      #zip creates a new list as it is a pure function, #izip computes the elements only when requested using iterator protocol but in python3, zip performs with the same functionality as zip
    print (f'{fruit} -> {vegetable}')

#with uneven list sizes
from itertools import zip_longest
for fruit,vegetable in zip_longest(fruits,vegetables, fillvalue='None'):
    print(f'{fruit} -> {vegetable}')

#-------> looping in sorted order
fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']

#5 bad
fruits.sort()                                       
for fruit in fruits:
    print (fruit)
print(fruits)                                       #this changed the original list, not a pure function

_fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']
#5 best
for fruit in sorted(_fruits):
    print(fruit)
print(_fruits)                                      #a pure function

#5 best reverse
for fruit in sorted(_fruits, reverse=True):
    print(fruit)

#5 best compare lengths
lengths = ['asd', 'dsgerg', 'rgsdgsdrwd', 'e', 'fw', 'reg', 'z']
print(sorted(lengths, key=len))

#-------> finding value in loops
#6 bad
users = ['parth', 'helly', 'nidhi', 'bhoomit']
found = False
find_name = 'nidhi'
for user in users:
    if user == find_name:
        found = True
        print("Found!")
        break
if not found:
    print("Not found!")

#6 better
users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
for user in users:
    if user == find_name:
        print("Found!")
        break
else:
    print("Not Found!")

#6 best
users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
print(f'User Found! at index: {users.index(find_name)}') if find_name in users else print("Not Found!")

#-------> delete item from dictionary while iterating
#7 bad
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in my_dict:                                   #deleting while iterating may cause abnomalities or error
    if key.startswith('b'):
        del my_dict[key]
print(my_dict)

#7 best
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in list(my_dict):                             #list(my_dict) is now a list of key values
    if key.startswith('b'):
        del my_dict[key]
print(my_dict)

#-------> looking over dictionary key and value
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}

#8 bad
for key in my_dict: 
    print(f'{key} -> {my_dict[key]}')                #need to rehash every key and go lookup on it         

#8 best   
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key, value in my_dict.items():                   # in python 2, my_dict.iteritems() would have been a better option than items(items is a pure function and hence makes a seperate new list and consume more memory) but now iteritems have been renamed to items in python 3 
    print(f'{key} --> {value}')


#-------> creating dictionary from two lists
users = ['parth', 'helly', 'nidhi', 'bhoomit']
fruits = ['apples','ginger' ,'bananas']                #dict([('1','2')]) syntax

#9 best
my_dict = dict(zip(users,fruits))                      #izip was better but is replaced to zip in python 3 which uses the same iterable protocol and uses single tuple
print(my_dict)

#-------> Merging two dicts
x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z={**x, **y}
z           #last value of repeated-b will be considered if duplicates in key are present

#-------> grouping items by length into a dictionary
users = ['parth', 'helly', 'nidhi', 'bhoomit']

#10 bad
d = {}
for user in users:
    key = len(user)
    if key not in d:
        d[key] = []
    d[key].append(user)
print(d)

#10 better
users = ['parth', 'helly', 'nidhi', 'bhoomit', 'zeal', 'zeel', 'uttam', 'vaikunth', 'shlok']
d = {}
for user in users:
    key = len(user)
    d.setdefault(key,[]).append(user)       #set default key,value just as defaultdict does
print(d)

#10 best
users = ['bhoomit', 'parth', 'helly', 'nidhi', 'zeal', 'uttam', 'vaikunth', 'shlok']

from collections import defaultdict
d = defaultdict(list)
for user in users:
    key = len(user)
    d[key].append(user)
print(d)

#-------> bonus: #reversing one-to-one dictionary
# bad
eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = dict()
for x,y in eng_to_span.items():
  span_to_eng[y] = x
span_to_eng

#best
eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = {v:k for k,v in eng_to_span.items()}
span_to_eng

#-------> bonus: #reversing one-to-many using default dictionary
e2s = {                         #this is very common arrangement of data, even if you look into google for a word's meaning, you'll get one key search word and a list of results associated with it
    'one':['uno'],
    'free':['libre','gratis']
}

#best
from collections import defaultdict
from pprint import pprint
s2e = defaultdict(list)
for k,listt in e2s.items():
    for v in listt:
        s2e[v].append(k)
pprint(s2e, width=40)

#-------> clarify names in function calls
def fun(username, password, is_premium_user):
    pass

#11 bad
fun('Parth',"2sf6h", True)

#11 best
fun(username="Parth", password="2sf6h", is_premium_user=True)

#-------> clarify multiple return values with named tuples
#12 bad
class_result = (9,1)
print(class_result)             #output does not make much sense while re-reading after a long time

#12 best
from collections import namedtuple
Class_Result = namedtuple('Result', ['passes','fails'])
#or
Class_Result = namedtuple('Result', [('passes',int), ('fails',int)])
class_result = Class_Result(9,1)
print(class_result)                 #now reading the output makes much more sense while re-reading
print(class_result[0])              #can acess value regularly
print(class_result.passes)          #can access value by it's name too, #seems similar to dictionary but has functionality of a tuple(immutablability)

#-------> unpacking sequences
my_tuple = 'hi','how','are','you'    #this is stored as a tuple
print(my_tuple)

#13 bad
p = my_tuple[0]
q = my_tuple[1]
r = my_tuple[2]
s = my_tuple[3]

#13 best
p,q,r,s = my_tuple

#-------> updating multiple state variables

#14 bad
def fibonacci(len_fib):
    x=0
    y=1
    for i in range(len_fib):
        print(x, end=', ')
        t = y
        y = x+y
        x = t
fibonacci(len_fib=10)

#14 best
def fibonacci(len_fib):
    x,y = 0,1
    for i in range(len_fib):
        print(x, end=", ")
        x,y = y, x+y                            #this way of calculating saves us from calculations the value updation problem i.e., current value, previous value, next value
fibonacci(len_fib=10)

#-------> concatenating strings
my_list = ['hi','how','are','you']

#15 bad
s = my_list[0]
for item in my_list[1:]:
    s += ", " + item
print(s)

#15 best
s = ', '.join(my_list)
print(s)

#-------> updating sequences

#16 bad
my_list = ['hi','how','are','you']
del[my_list[0]]
my_list.pop()
my_list.insert(0,"yo!")
print(my_list)

#16 best
from collections import deque
my_new_list = deque(['hi','how','are','you'])       #better data structure(less time complexity) to insert and remove items from front and end
del[my_new_list[0]]
my_new_list.pop()
my_new_list.insert(0,"yo!")
print(my_new_list)
my_new_list[0]
[*my_new_list]          #unpack the deque into simple list

#-------> open and close files
#17 bad
f = open('Some_Code.txt')
try:
    data = f.read()
finally:
    f.close()

#17 best
with open ('Some_Code.txt') as f:                   # resources are limited in supply, so using context managers is efficient because Only a certain number of files can be opened by a process at a time
    data = f.read()

#-------> how to use locks
import threading
lock = threading.Lock()

#18 bad 
lock.acquire()
try:
    print('Critical Section 1')
    print('Critical Section 2')
finally:
    lock.release()

#18 best
with lock:                                          #auto acquires the lock and releases it as it is handled by context manager 'with'
    print('Critical Section 1')
    print('Critical Section 2')

#-------> exercise: sum of squares first 10 numbers
#19 bad (shows how you can do it)
squares = []
for number in range(10):
    squares.append(number**2)
print(f'sum :{sum(squares)}')

#19 better (shows single unit of thought)
print(f'sum :{sum([x**2 for x in range(10)])}')     #using loop comprehension

#19 best
print(f'sum :{sum(x**2 for x in range(10))}')

#-------> form large list with same element multiple times
from collections import Counter     #for visualising purpose

#20 bad
my_list = ["list_item" for x in range(10)]
my_list
Counter(my_list)

#20 best
my_list = ["list_item"]*10
my_list
Counter(my_list)


#-------> Summing
#21 bad
sum([0.1]*10)
sum([0.1]*10) == 1         #this should have been true but due to precision points, it adds in precision point system

#21 best
from math import fsum
fsum([0.1]*10)
fsum([0.1]*10) == 1         #this rounds up and again the commutative properties are alive, this is used while doing data analytics

#-------> Printing
from collections import defaultdict
d = defaultdict(list)
d['p'].append('parthiv')
d['z'].append('zeal')
d['p'].append('parth')

#22 normal
print(d)

#22 best
from pprint import pprint
pprint(d, width=40)

#-------> Deflating matrix
m=[
    [10,20],
    [30,40],
    [50,60]
]

#23 bad
for row in m:
    for column in row:
        print(f'{column}', end=", ")

#23 best
print([x for row in m for x in row])


# Sample Input: abcdefghi -> abc def ghi

# Make string iterable as object
s = 'abadffghi'
list(zip(s,s,s))

s = 'abadffghi'
it = iter(s)
list(zip(it,it,it))     # __next__ is called each time the 'iter' object is called and the updated position value is provided

for part in zip([iter('abadffghi')]*3):
	print(part)

di = dict({'a':1,'b':2})
di.setdefault('c',3)    # -> 3, used setdefault because we're appending key,values

list(zip(['abc','def','ghi']))
list(zip(*['abc','def','ghi']))

for part in zip(*[iter('abadffghi')]*3):
    di = dict()
    "".join([di.setdefault(char,char) for char in part if char not in di])