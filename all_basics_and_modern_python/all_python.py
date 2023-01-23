#Chapter 1 : fundamental data types
#int
#float -> needs larger memory as single decimal value is stored into two seperate locations i.e., values before and after the point
#bool
#str    'immutable'
#list   'mutable'
#tuple  'immutable'
#set    
#dict   'mutable'
#defaultdict
#Counter
#complex




# $Classes -> custom types


# $Specialised data types -> that we don't want to create

# $
#None

# $Starting practice sessions
print("\nBasic Math operations")
print(2+3)                                       # 5
print(2-3)                                       # -1  
print(2*3)                                       # 6
print(2/3)                                       # 0.66
print(2//3) # -> integer                         # 0
print(2%3)                                       # 2
print(2**3) # 2^3                                # 8 

print("\nChecking the data type")
print(type(2/3))


# $Some Math functions
print("\nSome math functions")
print(round(3.7))                                 #returns 4
print(abs(-20))                                   #returns 20

# $Operator precedence
# 1.()
# 2. **
# 3. *,/
# 4. +,-
print("\nChecking operator precedence")
print( 2 + 3*4 )
print( (2 + 3) + 2**3 )

# $Binary
print("\nConverting to the binary representation and back")
print(bin(5)) #'0b'->represents that it is a binary format
print(int('0b101',2))


# $Variables -> also called binding values
# $use snake_case convention
print("\nUsing variables")
normal_variable = 10
print(normal_variable)

# $Another effective way to assign variables
a,b,c = 1,2,3
print("\na: ",a, ", b :",b)

print("\n'_' in the beginning generally signifies it's a private variable in python")
_normal_variable = 20
print(_normal_variable)


# $Constants -> general convention in CAPITALS
PI = 3.14
print("\n'__variable is known as a dundar in python")
# $so it's not a good practice to have '__' in variable naming convention



# $Expression and Statements
iq = 200
user_age = iq/5   
#'iq/5'            -> is a expression                  #'user_age = iq/5' -> is a statement



# $Augmented assignment operators
some = 5
some +=2
print("\nAugmented operation value :", some)



# $Let's try 'long string' AS DOC STRING
long_str = '''Im Yash
0 0
 _
'''
print("\nThis is the example of a long string")
print(long_str)
# $It can be used to print paragraphs,etc


# $Escape characters
print('\nTrying out the escape characters')
print ('It\'s a beautiful day')
print('\tIts a beautiful day')


# $Formatted Strings
print('\nTrying out formatted strings.')
name = 'Parth'
age = 24
print("Welcome " + name + ". You are "+ str(age) + " years old.")       #print like this
print("Welcome ", name , ". You are ", str(age) , " years old.")        #also can print like this
# $print needs strings, so convert everything in it to strings

print(f"Welcome {name}. You are {age} years old.")                      #also can print like this
print("Welcome {}. You are {} years old.".format(name,age))
print("Welcome {1}. You are {0} years old.".format(name,age))
print("Welcome {_name}. You are {_age} years old.".format(_name="P",_age=25))



# $String manipulation
# $string[start:stop:stepover]
print('\nManipulating Strings')
strin = '01234567'
print(strin[0])
print(strin[0:])
print(strin[:5])
print(strin[0:4])
print(strin[0:8:1])
print(strin[0:8:2])
print(strin[-1]) #index starts from last -1->0 from last
#print(strin.reverse()) ->string cannot be reversed but list can be like this
print(strin[-2])
print(strin[::-1]) #to reverse the string


# $Immutability
strin = '01234567'
#strin[0] = '8'  ->we cannot alter the string characters since string is 'immutable' just as a 'tuple'
#we can replace the whole string but not particular characters, once assigned is assigned 
strin = strin+ '8'
print(strin)


# $Boolean
print('\nWorking with booleans')
print(bool(0))
print(bool('True'))         #if casting is possible, interpreter will definately be able to cast it
print(bool(True))

#python has shor-circuting operator 'and' i.e., if the first value is true, it'll check the other value, but if the first value is false, the result has to be false and hence does not check the second value, however, if the first value(default/casted) is true and so is the second value, print statement will print the default value of the second object rather than True or False
True and True
True and False
False and True
bool('hello')   #stuff len>1 is True
bool('')
'' and 'hello' #did not even check 'hello' and printed the actual object rather than true/false
'asd' and 'hello' #checks both are true and prints the last object rather than true/false


# $Most common type conversion error
year = input("\nEnter your birth year :")
age = 2022 - int(year) #this is the part where error occurs most of the time 
print(f"Your current age is {age}")


# $Exercise password asterisk
u_name = input("\nEnter the username :")
password = input("Enter the password :")

print(f"Welcome {u_name}, your password :{len(password)* '*'} is {len(password)} letters long")



#Chapter 2 : working with lists 1
# $Working with lists
print('Working with lists')
li = [1,2,3]
li2 = ['a','b','c']
li3 = [1, 2.5, 'c', True]   #it can also hold values of multiple categories
print(li)

# $Unlike strings, list in not immutable i.e, it is mutable (we can change the sub element of the list)

li[1] = 2.5
print('\nNew list')
print(li)

# $Copying list problem
# $it can only done through list slicing
print("\nList copying problem")
cart = ['apple','banana','carrot']
new_cart = cart
new_cart[0] = 'orange'
print(cart)
print('This changed the original cart as it was assigned to it directly instead of slicing and copying, so the original list reference was assigned to the new variable')

print('\n\nThe correct way is by slicing the list or using the copy method')
cart = ['apple','banana','carrot']
new_cart2 = cart[:]
#new_cart2 = cart.copy()      #or by using inbuilt list method
new_cart2[0] = 'orange'
print(cart)



# $appending to a list returns no ValueError
print('\nAppending the list problem')
eg = [1,2,3,4,5]
eg2 = eg.append(100)
print(eg)
print("eg2 : ",eg2) #this will contain None

# $first we need to append seperately as append inPlace=True(according to some methods), just changes the list, does not return anything, similarly 'insert' does inPlace=True i.e., just modifies whatever is in the memory
eg = [1,2,3,4,5]
eg.append(100)          #we can only append one item at a time
eg2 = eg[:]
print("eg2", eg2)

eg.append([100,200])  #this appends a list as single element inside original list
print(eg)

#so to append multiple values, we can use 'extend' and items as a list
eg.extend([200,201]) #takes iterable list as input unlike append
print("eg", eg)



# $Remove(by value) and pop(by index/last element)
eg.pop()
print("eg :", eg)
eg.pop(0)
print("eg :", eg)
p = eg.pop(2) #takes 'index' and returns whatever you just removed
print("eg :", eg , ", Pop value :", p)

eg.remove(5) #takes 'value' and removes it, this also works inPlace=True
print("eg :", eg)

eg.clear() #clears everything from the list
print(eg)

eg = ['a','b','c','d','e','d']
print("index of 'd' is :",str(eg.index('d')))
print("count of 'd' is :", str(eg.count('d')))
print("Is 'd' present in the list 'eg' : ", 'd' in eg)
print("Is 'a' present in 'hello world' ", 'a' in 'hello world')


# $Sorting the lists
print("\nSorting by 2 ways")
eg = ['z', 'a', 'v', 's', 'p']
print("'sort' is inPlace :", eg.sort())   #returns None as inplace=true for this method
print(eg)

eg2 = ['z', 'a', 'v', 's', 'p']
print("'sorted' is not inPlace :",sorted(eg2))

print("\nReversing the list")
print("Original :", eg2)
print(eg2.reverse())  #inplace=True
print("REversed :",eg2)

sorted([5,2,1])
sorted([7,4,9] + [12,7,32])
sorted([1,4,7] + [4,9,12] + [33,76,99])   #sub lists are already sorted, use a better data structure


# $a better approach for sorting long sorted sublists is using merge
from heapq import merge
a = [1,4,7] 
b = [4,9,12] 
c = [33,76,99]
it = merge(a,b,c)      #gives a generator object, an iterable object, a generator is a kind of iterator that runs on demand
list(it)
next(it)               #if you multiple sorted long lists and you need to get first few elements, prefer using merge
next(it)       


# $islice 
# $seems as regular slicing but can also consumes an iterable object and yields an iterable object to save memory along with regular lists
from itertools import islice
islice('abcdef',3)            
list(islice('abcdef',3))        #0,stop
list(islice('abcdef',None,3))   #0,stop
list(islice('abcdef',2,4))      #start,stop
list(islice('abcdef',2,6,2))    #start,stop,step

a = [1,4,7] 
b = [4,9,12] 
c = [33,76,99]
it = merge(a,b,c)
list(islice(it,3))    #suppose you have google qeury responses to show, millions of results, use 'merge' with 'islice' to process only generators and showing content with islice as per as page limit and stuff...
list(islice(it,None)) #returns complete list

# $intern values
# $assign same memory location(& only one) to all strings that are same(lookwise)
s = 'he'
t = 'llo'
u = s+t
w = 'hello'

u,w
u==w              #check the value at the variable reference point
id(u),id(w)       #different references, consumed double memory for single object
u is w            #compares actual reference addresses

import sys
u = sys.intern('hello')
v = sys.intern(s+t)
u is v
id(u),id(v)       #now we did not create redundant data memory, but used reference names to a single memory location
# usecase, don't allow redundant usernames

''''done till here 21 nov 22'''

#Chapter 3 : working with lists 2
# $More with lists
basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) #inplace=False with to slicing
print("Recersed list   :", basket)

# $Creating list with range
# range is an generator
print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))

# $Range in loops
print("\nRange functionality")
for number in range(5,8):
  print(number)

print("Range with stepovers")
for number in range(1,10,3):
  print(number)

print("If we don't really need variable")
for _ in range(5,8):
  print(_)

print("Creating lists using range")
for _ in range(0,2):
  print(list(range(10)))


# $join
print("\nJoin operation")
sentence = '-'
print(sentence.join(['hi','my','name','is','Parth']))   #does not add before first and after last
print(' '.join(['hi','my','name','is','Parth']))

# $split, default split is by white space
'Hello there, how are you'.split()

# $List unpacking
print("\nList unpacking")
a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)

# $bisect
# $using dictionary proves to be a better searching tool than bisect as it uses hash
#default bisect is bisect right
# used : searching ranges given end points 
import bisect
cuts = [20,40,60,80]
grades = 'EDCBA'
grades[bisect.bisect(cuts,50)]
[grades[bisect.bisect(cuts,x)] for x in [10,30,50,80,100]]


# $Chapter 4 : Dictionary
# $Dictionary -> key,value pairs
# $The keys can be all those objects that are immutable, like strings, booleans but not lists
#keys need to be unique, if not, the last key will override all the other previous keys
print("\nDictionary")
dictionary = {
  'a': [1,2,3],
  123: 'hello integer',           #First key of all same keys will be selected as key and last updated value as the value for the first key
  123.0:'hello float',  
  123.12:'hello double',
  False: True
}
print(dictionary)
print(dictionary['a'])
print(dictionary.get('a',"default_value"))
print(dictionary[123])        #prints float value (if a similar float present)
print(dictionary[123.0])      #prints float value

# $Another way to create a dictionary
dictionary2 = dict(a=[1,2,3], b="asd")    #a,b are taken as key in form as strings
print(dictionary2)
print(dictionary2['b'])

# $Creating list with dictionary
print("\nList with dictionary")
my_list = [
  {
  'a': [1,2,3],
  'b': 'hello',
  'c': True
  },
  {
  'a': [4,5,6],
  'b': 'world',
  'c': False
  }
]

print(my_list[1]['a'])



# $Eliminate error if key not present in the dictionary
# print(my_list['age'])->this will give error and stop the program after this
dictionary = {
  'a': [1,2,3],
  123: 'hello integer',
}
print(dictionary['age'])          #call by key directly returns 'KeyError' error
print("Returns 'None' in absence of key \"age\": ", dictionary.get('age'))  #call by it's method returns None
print("Returns default if key not present else returns the actual value: \n",dictionary.get('age','default_Age'))

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value
print(dictionary.setdefault("b","b set from default"))
print(dictionary)

# $Or else you can check for a key another way
print("Check for the presence of key 'a' :", 'a' in dictionary)                                     #checks only in keys by default always(simple dictionary object)
print("Check for the presence of value 'hello' :", 'hello' in dictionary)         
print("Check for the presence of value 'hello integer' :", 'hello integer' in dictionary)           #does not check in values by default
print("Check for the presence of key 'a' :", 'a' in dictionary.keys())                              #specify search criteria
print("Check for the presence of value 'hello' :", 'hello' in dictionary.values())
print("Check for the presence of value 'hello integer' :", 'hello integer' in dictionary.values())  #specify search criteria

print(type(dictionary))
print(type(dictionary.items()))
print("Get whole dictionary items in a list(couple):", dictionary.items())
print("Check for the presence of any item(key/value) 'hello integer' :", 'hello integer' in dictionary.items()) #->gives us false. can't do this

dictionary3 = dictionary.copy()
print("dictionary after copying : ", dictionary3)
dictionary.clear()
print("dictionary after clearing : ", dictionary)
print("Pop key value pair :", dictionary3.pop('a'))
print("dictionary3 : ",dictionary3)


# $Update a Value
print("Updating key(123) :", dictionary3.update({123:'hell'})) #inplace=True
# $inserting via update method
print("Updating key(123) :", dictionary3.update({'zebra':'black'})) #inplace=True
print("dictionary3 : ", dictionary3 )


# $Iterating dictionary
dictionary = {
  'a': [1,2,3],
  123: 'hello',
  False: True
}

print("\nIterating the dictionary simply")
for item in dictionary:         #as always, simple dictionary object is linked only with keys
  print(item) #prints the 'keys'

print("\nIterating the dictionary by keys")
for item in dictionary.keys():
  print(item) #prints the 'keys'   

print("\nIterating the dictionary by items")
for item in dictionary.items():
  print(item) #prints the tuple of couples  
  key,value = item #gets value from tuple
  print(key, " : ", value)

print("\nIterating the dictionary by items")
for key,value in dictionary.items(): #gets value from tuple directly
  print(key, " : ", value)  

print("\nIterating the dictionary by values")
for item in dictionary.values():
  print(item) #prints the 'values'    


# $Default dict -> Slight modification of dict except it never raises a 'KeyError'
# $It provides a default value for the key that does not exists.
from collections import defaultdict
#uses: Grouping, accumulation, reversing one-to-one dictionary, reversing one-to-many dictionary
# Function to return a default 
# values for keys that is not 
# present 
def def_value(): 
    return "Not Present"
      
# Defining the default dict 
d = defaultdict(def_value)  #define here what should be the output when key not found as a higher level function name
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"])     #this key not present, so default dict will create this new key with the value defined by function specified during it's declaration time

#or
d = defaultdict(lambda:"Not Present")

#therefore now we can also use default dict to group things together
d = defaultdict(set)
d['starts_with_l']
d['starts_with_p'].add('parth')
d['starts_with_l'].add('lathiya')
d['starts_with_l'].add('lavjibhai')
d

# $Excersize ->sum list members
print("\nIterable sum example")
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for item in my_list:
  sum+=item
print("Total sum of all items = ",str(sum))

#another way to solve(using range)
another_sum = 0
for index in range(len(my_list)):
      another_sum += my_list[index]
print(f'Another Sum : {another_sum}')


# $Enumerate
print("\nEnumerate example")
for item in enumerate("Hellooo"):
  print(item)                   #returns tuples of couples with (index,char)

print("Main purpose -> to get the index from 0")
for index, item in enumerate("Hellooo"):
  print(f'{index} -> {item}')            #hence we can retrive both seperately

print("Main purpose -> to get the index from custom index")
for index, item in enumerate("Hellooo", start=1):
  print(f'{index} -> {item}')            #we can enumerate by specifying the start position as well


# $While loops
print("\nChecking while loops")
i=0
while i<2:
  print("i : ", str(i))
  i+=1
else:
  print("done with all the work")  

i=0
while i<50:
  print("\ni : ", str(i))
  break     #breaks out in the first iteration itself without even running 'else' part
else:
  print("done with all the work")   #does not runs after break, 'else' is used only if the whole loop completes without any break successfully and we need to show some message

# $While example
while True:
  response = input("Chat 'bye' to exit :")
  if("bye" in response.split()):
    break

# $'continue' example
# $skip if you get '3'
print("\nSkipping no. 3")
for item in [1,2,3,4,5]:
  if(item == 3):
    continue
  else:
    print(item)

# $'pass' example
# $it is absolutely nothing, if you're using for loop and you don't know what to right, indentation error will arise. Thereyou can use pass as a placeholder
for x in [1,2,3]:
  pass

#iterator magic
#(partially consumed iterable)
it = iter('abcdefg')        #make anything iterable, now it follows iterable protocol with additional tools as 'next', etc.
next(it)
next(it)        #not only it iterates element one by one but it is halted at that place, see by making the list with the rest of the iterator object
list(it)        #surprise, this is helpful if you want to parse the incomming header with the id and iterate over the received data


# Chapter 5 :
# $Starting with tuple -> immutable
# $therefore it can be used as a key in the dictionary and not the list(which is mutable)

my_tuple = (1,2,3,4,5) #faster than list. use for unchangabe items and security

# $This won't work because list is mutable
# user = {
#   [1,2] : [1,2,3],
#   'greet' : 'hello',
#   'age' : 24
# }

user = {
  (1,2) : [1,2,3],
  'greet' : 'hello',
  'age' : 24
}

print("Calling value using tuple(as key)",user[(1,2)])


# $tuple stuff
new_tuple = my_tuple[:]
x,y,z, *other = new_tuple
print("\nSlicing tuple :", my_tuple[2:3])
print("Slicing tuple :", my_tuple[2:])
print("x : ",x)
print("y : ",y)
print("z : ",z)
print("other : ",other)
print("Count '5' occurances: ", new_tuple.count(5))
print("Index of '5' occurance: ", new_tuple.index(5))
print("Length of the tuple :", len(new_tuple))



# Chapter 6 : Sets
# $unordered collections of unique sets
#sets will always return themselves(after defining) as sorted, with unique items

my_set = {1,2,3,4,5}
print("my_set : ", my_set) #ascending

my_set = {1,5,3,4,5,5,2,5,5,5}
print("my_set : ", my_set) #ascending

# $convert a list into a set
my_list = [9,4,5,4,4,2,2,1]
my_list_set = set(my_list)
my_list_back = list(my_list_set)
print("\nList converted to set :", my_list_set)
# $useful in sending emails to a list containing duplicate emails

# $Exercise -> count each element's count in a list
exe_list = [1,5,3,1,6,9,6,4,6,2,5,8,4,2,4,7,8,9,4,2,1,6]
for item in exe_list:
      print(f'element: {item} : count: {exe_list.count(item)}')

# $Exercise -> count each element's count in a list more effectively(without implementing count function on the same element >twice)
exe_list = [1,5,3,1,6,9,6,4,6,2,5,8,4,2,4,7,8,9,4,2,1,6]
exe_set_list = list(set(exe_list))
for item in exe_set_list:
      print(f'element: {item} : count: {exe_list.count(item)}')

print("\nLength of my_list(set) :", len(my_list_set))
print("Check an item '4' in my_list_set:",4 in my_list_set)


my_set = {9,4,5,4,4,2,2,1}
new_set = my_set.copy()
my_set.clear()
print("\nOriginal(my_set) after clearing : ", my_set)
print("new(new_set) after clearing : ", new_set)


# $Set's methods#
#################
#Remember the venn diagram
#################
# .difference()
# .discard()
# .difference_update()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print("\nSet operations/methods")
print("Difference :", my_set.difference(your_set)) #just tells us the differemnce, not update the set #remove common things from me
print("Difference :", my_set.difference_update(your_set)) #finds the differemce and updates the original set #inPlace=True
print("my_set : ",my_set)
print("Discard : ", my_set.discard(1)) #inplace=True
print("my_set after discarding '5' : ",my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print("Intersection :", my_set.intersection(your_set)) 
print("Intersection(another method) : ", my_set&your_set)
#common things

print("\nDisjoint(is there anything common. are they not overlapped?) : ", my_set.isdisjoint(your_set))

my_set = {1,2,3}
your_set = {4,5,6,7,8,9,10}
print("Disjoint(is there anything common. are they not overlapped?) : ", my_set.isdisjoint(your_set))
print("True: They are not overlapped(they are dis-joint)")


print("\nUnion : ", my_set.union(your_set))
print("Union(another method) : ", my_set|your_set)

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print("\nis x subset of y? :", my_set.issubset(your_set))
print("is x superset of y? :", my_set.issuperset(your_set))
print("is y superset of x? :", your_set.issuperset(my_set))


basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) #inplace=False due to slicing
print("Original list   :", basket)

# $Creating list with range
print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))


# $join
print("\nJoin operation")
sentence = '!'
print(sentence.join(['hi','my','name','is','Parth']))
print(' '.join(['hi','my','name','is','Parth']))


# $List unpacking
print("\nList unpacking")
a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)


# Chapter 7 : working with lists 3
#  # More with lists
# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
print(basket.remove('Banana'))
print(basket)
# 2. Remove "Blueberries" from the list.
print(basket.pop())
print(basket)
# 3. Put "Kiwi" at the end of the list.
print(basket.append("Kiwi"))
print(basket)
# 4. Add "Apples" at the beginning of the list
print(basket.insert(0,"Apples"))
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))
# 6. empty the basket
print(basket.clear())
print(basket)


# Chapter 8 :
# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

print(basket[1][1][0])


# Solution:
# basket[1][1][0]


# Chapter 9 : Operator Precedence
# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)
#450

print(((5 + 4) * 10) / 2)
#45
print((5 + 4) * (10 / 2))
#45
print(5 + (4 * 10) / 2)
#25
print(5 + 4 * 10 // 2)
#45


# Chapter 10 :String Formatting
# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? (Scroll down for answer)
name='cindy'
amount=50
print(f"hello {name}, your balance is {amount}")

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")



# Chapter 11 : Miscelleaneous
# $Condtions
# $Truthy and Falsy

x,xx = "Hello",""
y,yy = 20,0

print(f"x:{bool(x)}, xx:{bool(xx)},\ny:{bool(y)}, yy:{bool(yy)}")

# $Check is username or password exists
username = "Parth"
password = '123'

if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")

username = "Parth"
password = ''
print("Current password :", bool(password))
if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")

# $Ternary operator
#Note: Ternary operator returns only expressions on both sides, statements are NOT allowed
is_friend = True
can_message = "message allowed" if is_friend else "message not allowed"
print("\ncan_message :", can_message)

#Failed eg.
# li = [(1,2), (2,2), (3,1)]
# res = [0, 0]
# for x,y in li:
#       res[0] += 1 if x > y else res[1] += 1  #cannot assign in ternary operators
# #Sol for Failed eg
# for x,y in li:
#       r = 0 if x > y else 1
#       li[r]+=1
      


# $Wizard if else
is_magician = False
is_expert = True
if is_magician and is_expert:
  print("\nYou are a master magician")
elif is_magician and not is_expert:
  print("\nAtleast you're getting somewhere")
elif not is_magician:
  print("You need magic powers")

# $is vs ==
print("\n'is'-> compares content at the passed value memory location")
print(True is True)
print('1' is '1')
print([] is []) #data structures are created at different locations
print(10 is 10)
print([1,2,3] is [1,2,3])

# $concept
a = [1,2]
b = [1,2]
memory = "Same memory" if a is b else "Different memory"
print("\nMemory location : ", memory)

print("\n'=='-> compares content")
print(True == True)
print('1' == '1')
print([] == []) #data structures are created at different locations, but currently content is same
print(10 == 10.0)
print([1,2,3] == [1,2,3])

# $Loops
# $Iterable ->list,dictionary,tuple,strings,set
print("\nFor loop")
for item in "Hi Duh!":    #'ji duh!'->is an iterable item
  print(item)

for item in reversed("Hi Duh!"):
      print(item)

for item in [1,2,3]:    
  print(item)

for item in {1,2,3}:    
  print(item)  

for item in (1,2,3):    
  print(item)



  #Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for row in picture: #name as readable/rememberable as possible
  for pixel in row:
    # if pixel == 0:  #you can clean it
    if not pixel: 
      print(" ",end='') #we need this to override the default end='\n' from the print
    else:
      print("*",end='')
  print("\n")    


# $Some excersize 
# $Create a new list indicating multiple entrie items
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []

for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicates:
      duplicates.append(item)
  
print(duplicates)



# $Functions ->takes parameters
# $Methods ->are a part of objects
# $Generic
def call_me():
  print("You have called me!")

print(call_me)  #function name and memory location
call_me()


# $Positional arguments->position matters in argument
def call_me(name,age):  # <-this is parameter
  print(f"\nYou have called me {name}! of {age} age")

call_me("Parth",24) # <- this is argument 

# $Keyword arguments #('can be confused with default arguments)
call_me(age=25, name="Zeal")  # <-bad practice


# $Default parameters
def call_me(name="Default",age=25):  # <-this is parameter
  print(f"\nYou have called me {name}! of {age} age")

call_me()

# $calling function inside of a function
def outer_function():

  print("\nOuter function`")
  def inner_function():
    print("\nInner function")

  return inner_function()

outer_function()


# $'*args' and '**kwargs'
# $passing any number of arguments as 1 parameter

# def some_fn(args):
#   return sum(args)

# some_fn(1,2,3,4,5)  # <=this will give error as some_fn above only takes one argument

def some_fn(*args):   # -> args stored as tuple
  return sum(args)

print("\n'args' gets stored as a tuple, Sum :",some_fn(1,2,3,4,5))


# $using '**kwargs'
def some_fn(**kwargs):
  print(kwargs)
  print(kwargs['item1'])
  return sum(kwargs.values())

print("\n'kwargs' contains a dictionary, Sum :",some_fn(item1=5, item2=10))



# $Combination of all
# $Rule: params, *args, default_params, **kwargs
def some_fn(name,*args,age=24,**kwargs):
  return sum(kwargs.values()) + sum(args)

print("\nCombination :",some_fn('Parth',1,2,3,4,5,25,item1=5, item2=10))


# $partials (freeze the function and reduce the number of parameters by assigning some parameters by default)
from functools import partial

pow(2,5)  #this is an inbuilt function
two_pow = partial(pow,2)    #passed one argument and freezed it into a variable
two_pow(5)    #call the freezed partial function with the remaining arguments




# $Scopes
#1 local
#2 Parent local
#3 Global

# $variable scope confusing example 

# $ ->local eg. (a variable defined inside a new scope has its own scope)
print("\nScope Confusion")
a=1
def fn():
  a=10
  return a
print(fn())  
print(a)

# $'nonlocal' keyword eg. (a variable defined with non local has it's parent's scope)
def outer():
  x = 'local'

  def inner():
    nonlocal x  #<- don't use if not required
    x = 'non local'
    print("\nInner x : ",x)
  inner()
  print("\nOuter x : ",x)

outer()


# $Example exercise for function
def highest_even(li):
  highest=0
  for item in li:
    new=item/2
    if(item%2==0 and new > highest):
      highest=new
  print("\nHighest Even : ",highest*2)

highest_even([10,2,5,3,79,4,80])



# $Class
# $'self' is compulsory in all functions
class PlayerCharacter:

    membership = True

    def __init__(self, name):  #<-'self' is necessary
        self.name = name
        print("\nMembership :", self.membership)
        print("Membership :", PlayerCharacter.membership)

    @classmethod
    def classMethod(cls, num1, num2):  #<-'cls' is necessary  #because it returns a new class object
        return cls("Uttam")

    @staticmethod
    def staticMethod(num1, num2):
        return num1 + num2

    def run(self):  #<-'self' is necessary for accessing the class variable in the method declaration
        print(f"\n{self.name} is Running")  #<-'self' needed


player1 = PlayerCharacter("Parth")
player2 = PlayerCharacter("Zeal")
print("Player 1 :", player1.name)
print("Player 2 Membership:", player2.membership)
print("Player Membership :", PlayerCharacter.membership)
player2.run()
print("\n", player2.run())  #<-returns nothing (it prints it's stuff but returns nothing, obvious)

player3 = PlayerCharacter.classMethod(2, 3)
print(
    "\nCalling class method and getting new player object with 'cls' method and getting name :",
    player3.name)
print("\nCalling static method :", PlayerCharacter.staticMethod(2, 3))

# $There is no true privacy(public/private)
# $we can tell ourselves by using conventions of private so that we don'e end up changing them


class Dog():

    _animal_type = 'Dog'

    def __init__(self, breed, speed):
        self._breed = breed
        self._speed = speed

    def run(self):
        print(f"\n'{self._breed}' dog is running at {self._speed} km/hr")


dog1 = Dog("joshua", 12)
print("Dog1 animal type : ", dog1._animal_type)
dog1.run()

# $We can also alter the class methods and attributes
dog1._animal_type = 'Cat'  #<-we should not change private attributes which are denoted by '_'
print("Dog1 animal type : ", dog1._animal_type)

# $we can also alter method strangly
dog1.run = 'hello'
print("Dog1 run method converted :", dog1.run)

# $Inheritence
print("\nInheritence example")

#class User(object): #<-every class inherits from 'object' class by default and methods of object class are the 'dundar' methods ones with '__xyz__' schema
class User():
    def sign_in(self):  #<- 'self' is necessary
        print("Signed in")


class Wizard(User):  #<- provide 'Super' class in parameter to inherti
    pass


class Archer(User):
    pass


wizard = Wizard()
print("Wizard signed in!", wizard.sign_in())    #print returns none ofcourse as method does not return anything
archer = Archer()
print("Archer signed in!", archer.sign_in())    #print returns none ofcourse as method does not return anything


# $'isinstance' and 'issubclass'
print(f"\nIs wizard an instance of Wizard class? {isinstance(wizard,Wizard)}")
print(f"Is wizard an instance of User class? {isinstance(wizard,User)}")
print(f"is wizard an instance of highest('object') class? {isinstance(wizard,object)}")   #object is the superclass of all objects
print(f"is wizard a subclass of highest('object') class? {issubclass(Wizard,object)}")



# $Super
# $accessing the super class attribute(not method, method can be called directly through Inheritence)
class A():
  x=10

  def __init__(self,type):
    self.type = type
    return self.type

class B(A):
  def __init__(self,name,type):
    super().__init__(type) #<-call the super init method like this

b = B("BBB","Human")
print(f"Class B's type : {b.type}")


class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals
        

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Cattie(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon("ccc",12),Sally('sss',10),Cattie('CCC',11)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()



# $Decorators
# $ability to use function names similar to variable calling(Higher Order Functions)
# $Note: map,reduce,filter,zip functions are all the higher order functions i.e., calls the passed argument functions
# $For example,
def call_fun(passedfun):
    return passedfun()    #->returns calling function

def greet():
    print('Calling \'fun\' as a variable')

greet()  #<-function passed as variable name

# $another way
def call_ref(passedfun):
    return passedfun     #->this time returns reference only, does not call

def greet():
    print('Calling \'fun\' as a variable')

call_fun(greet)  
x = call_ref(greet)       
x()                     #<-therefore calling returned reference seperately from before

# $Come to creating decorators
# $Remember these super charges any function i.e., make it more powerful
print("\nCreating our own decorators")
def my_decorator(func):               #<-my decorator(super charger), accepts higher order function
  def wrap_func():
    print("***************")
    func()
    print("***************")

  return wrap_func                    #-> should have returned just reference, but since it is used as a decorater, it's return statement will automatically call function

@my_decorator
def callll():
  print("Just callin!") #<-sequence of thier run in unstable

callll()


# $we can also call decorator as such
print("\nAnother method")
another_one = my_decorator(callll)  
print(another_one)

# $Decorators with arguments
print("\nCreating our own decorators with arguments")
def my_decorator(func): #<-my decorator(super charger)
  def wrap_func(greeting,emoji):
    print("***************")
    func(greeting,emoji)
    print("***************")

  return wrap_func

@my_decorator
def call_me(greeting, emoji):
  print(greeting,emoji)

call_me('Hello ', ':)')

# $More flexible way to do this
print("\nCreating our own decorators wit multiple arguments/types")
def my_decorator(func): #<-my decorator(super charger)
  def wrap_func(*args,**kwargs):   #here **kwargs is not used, these arguments are comming from the original function
    print("***************")
    print(args,"\n", kwargs)
    func(*args,**kwargs)
    print("***************")

  return wrap_func

@my_decorator
def call_me(greeting, emoji=':)'): #<-variable + default 
  print(greeting,emoji)

call_me('Hello ')



# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}
user2 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}



def authenticated(fn):
  def wrapper(*args, **kwargs):
    print(args[0])  #<-args is returned as a tuple
    if args[0]['valid'] == True:
      fn(*args, **kwargs)
    else:
      print("The user is not valid")  

  return wrapper  
  
@authenticated
def message_friends(user):
  print('message has been sent')

message_friends(user1)
message_friends(user2)

# $Time module
import time
time.sleep(5)
print("Printing after 5 seconds, count 1 missisiipie, 2missisipie, ...5missisipie")
time.time()     #for computer people
time.ctime()    #for non computer people


# $Measure performance of each function using decorator
from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args,**kwargs)
    t2 = time()
    print(f'Took {(t2-t1)*1000} seconds to complete')
    return result
  return wrapper

@performance
def my_function():
  for i in range(1000):
    i*2

my_function()

@performance
def my_function():
  for i in range(100000):
    i*2

my_function()    




# Performance of the generators
from time import time

def performance(fun):
  def wrapper():
    t1 = time()
    fun()
    t2 = time()
    print("\nTime to run : ", t2-t1, " seconds")
  return wrapper

@performance
def long_time():
  print("1", end="")
  for i in range(100000):
    i*2

@performance
def long_time2():
  print("2", end="")
  for i in list(range(100000)):
    i*2

long_time()
long_time2()


# $Use generators to save memory and time instead of lists
# $when you have to calculate things one by one

# $Comprehension of generators
# def gen_fn(num):
#   for i in range(num):
#     yield i

# # $comprehension
# for item in gen_fn(100)  :
#   print(item)

# $How 'range' works
print("\nHow 'range' works")
class MyRangeGen():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def __iter__(self): #<-say that this is an iteraator and that __next__ dundar works on it
    return self

  def __next__(self):
    if MyRangeGen.current < self.last:
      num = MyRangeGen.current                #current should be remembered as a class object
      MyRangeGen.current += 1             
      return num
    raise StopIteration

gen = MyRangeGen(0,5)
for i in gen: #<-'for' loop user 'next' and 'iter' dundar methods to run
  print(i)  

# $How 'for loops' work
print("\nHow 'for' works")
def special_iter(iterable):
  iterator = iter(iterable)             #'iter' is used to make anything iterable and allow next function to work on it
  while True:
    try:
      print(next(iterator))
    except StopIteration:
      break  

special_iter([1,2,3])  

# $fibonacci using generators
print("\nFibonacci using generator")
def fib(number):
  a=0
  b=1
  for i in range(number):
    yield a                             #'yield' is like return but sends out value and halts iteration at that point till 'next' is called which 'for' loop does
    temp=a
    a=b
    b=temp+b
for x in fib(5):
  print(x)


# $Generators
# $'range()' is a Generator

print("Range : ",range(100)) #<-takes much less memory
print("\nLisdt : \n",list(range(100))) #<-takes much memory

def create_list(num):
  generated_list = []
  for i in range(num):
    generated_list.append(i)
  return generated_list

print("\nGenerated list this way : \n",create_list(100)) #<-same as list(range(100))

# $Generators('range') can produce iterables('list'), but not vice-versa
# $your own genertor and 'yield'
print("\nOwn generator (and 'yield' functionality): ")
def generator_function(num):
  for i in range(num):
    yield i

g = generator_function(100)
print (f'G(once) : {g}')
print(f'G(next time) : {next(g)}')
print(f'G(next time) : {next(g)}')


# $Functional programming
# $Pure functions
# $         -should not change the outside data
# $         -should not have any side effects

my_list = [1,2,3]

def multiply_by2(listt):
  new_list = []
  for item in listt:
    new_list.append(item*2)
  return new_list

print(f"Multiply by 2 list : {multiply_by2(my_list)}")
print(f"my_list : {my_list}")
# $the original list was not altered ->i.e., good


# $map,reduce,zip, filter
''' 
   $ ('map' and 'filter') will call the function for every element in corresponding list and 
     pass list's value into called function, appending the results to 
      - map object for 'map'
      - filter object for 'filter' 
   $ Pass function name as higher order function
'''

# $map
# $Pass function name as higher order function
# $'map' is a pure function i.e., original list is not affected
# $there is another 'map' function in DataFrame.map that follows diff. syntax

# $Example 1
my_list = [1,2,3]
def multiply_by2(x):
  return x*2            #append this items in 'map' object

print("\nThrough mapping :",list(map(multiply_by2, my_list)))

# $Note: since we're passing higher order function, we can use lambda functions
print("\nThrough mapping :",list(map(lambda x: x*2, my_list)))

# $Example 2
my_list = ['surat', 'vadodara', 'ahmedabad']
print(list(map(str.upper, my_list)))

# $filter
my_list = [1,2,3]
def only_odd(x):
  return x%2!=0        #append 'True' items 'values' only in 'filter' object

print("\nThrough filtering :",list(filter(only_odd, my_list))) 


# $zip #<-zip each consecutive items of each iterable into a tuple and returns another list
my_list = [1,2,3]
your_list = [10,20,30]

print("\nThrough zipping :",list(zip(my_list,your_list)))


# $reduce (not a python built in function) #<-map,zip,etc are built with reduce
print("\nThrough reduce :")
from functools import reduce
my_list = [1,2,3]

def accumulator(acc,item):
  print(acc, item)
  return acc+item

print(reduce(accumulator, my_list, 0)) #<-0 is given as the initial value here



# $lamda functions #<-functions that we have to use only once and throw away
''' Usage: When we make function call as higher order functions'''
# $let's say we don't really need out memory to keep the function 'multiply_by2' since it has to be only performed once, so we change that function to a lambda function
# $ syntax : labda my_list_item: my_list_item*2
# $no name attached to lamda function, just input parameters and output action
# $ lambda parameter: action(parameter)

# $Example
print("\nUsing labda function")
my_list = [1,2,3]
print(list(map(lambda my_list_item:my_list_item*2, my_list)))
print(list(filter(lambda my_list_item:my_list_item%2==0, my_list)))
print(reduce(lambda acc,my_list_item:acc+my_list_item, my_list,0))

# $now using labda function, we just cleaned up a lot of code that occupies our file

# $Exercise lamda, square the list
print("\nSquare list using labda function")
my_list = [1,2,3]
print(list(map(lambda my_list_item:my_list_item **2, my_list)))


# $Exercise labda, sort using 2nd value of tuple in a list
print("\nSorting using 2nd item in tuple in list using labda function")
a=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key = lambda item_a: item_a[1])
print(a) 


def multiplexers():
	return [lambda n: index * n for index in range (4)]

print [m (2) for m in multiplexers()]




# $list,set,dictionary comprehension
# $Way to create data structures very fast
my_set1 = [char for char in 'Hello']
print(my_set1)
my_set2 = {value for value in range(1,10)}
print(my_set2)
my_set3 = {value*2 for value in range(1,10)}
print(my_set3)
my_set4 = {value**2 for value in range(1,10)}
print(my_set4)

print("\nList and set comprehension")
print(f'{my_set1}\n{my_set2}\n{my_set3}\n{my_set4}')

print("\nDictionary comprehension")
simple_dictionary = {
  'a':2,
  'b':5
}

new_dictionary = { key:value for key,value in simple_dictionary.items() if value%2==0} #<-interesting
print(new_dictionary)

# $Exercise, create a dictionary using comprehension with a list(k=listitem, v = listitem*2)
print("\nExample dictionary from list")
my_list = [1,2,3]
new_dictionary = {k:k*2 for k in my_list}
print(new_dictionary)

# $Exercixe, create newlist containing only repeated items from a list
print("Displaying items that are multiple from a list")
my_list = ['a','b','c','b','d','m','n','n']

duplicates=[]
new_list = set([item for item in my_list if my_list.count(item)>1])
print(new_list)


# context managers
# default context manager for file system 'with'
with open("Some_Code.txt") as f:
  data = f.read()

# $custom context manager for any type of operation eg., making database connections
# $this for file management  
class FileManager(): 
    def __init__(self, filename, mode): 
        self.filename = filename                #define required process arguments
        self.mode = mode 
        self.file = None
          
    def __enter__(self): 
        self.file = open(self.filename, self.mode)  #make connections/utilise resources
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback):   #dump resources and parameters handle execptions
        self.file.close() 
  
# loading a file  
with FileManager('Some_Code.txt', 'r') as f: 
    f.read() 
  
print(f.closed) 

# $bottle templates
from bottle import template

print(template('The answer is {{x}}', x=10))
print(template('The answer is {{x**2}}', x=10))

lastname= 'lathiya'
first_names = 'parth twinkle chirag'.split()
family_template = '''The {{lastname.title()}} Family'''
print(template(family_template, lastname=lastname))

new_family_template = '''The {{lastname.title()}} Family
{{'=' * (len(lastname)+11)}}'''
print(template(new_family_template, lastname=lastname))

#Note: '%' symbol is used to run statements, we use {{}} for running expressions
whole_family_template = '''The {{lastname.title()}} Family
{{'=' * (len(lastname)+11)}}
%for firstname in first_names:
* {{firstname.title()}}
%end
'''
#we need to specify end because we are using template
print(template(whole_family_template, lastname=lastname, first_names=first_names))

# $Testing
# test with: mypy: for type checking
#      with: pyflakes: for redundant/missing imports and spelling mistakes
#      with doc test: to check the documentation example
#      with: pytest: for checking corner test cases
# use itertools to apply test case scenerios for pytest
from itertools import *     #import *'s only in terminals to reduce typing work, not in actual python files
for t in product('ABC', 'DE', 'xyz'):
      print(t)    #returns 3*2*3 results
for t in permutations('Love'):
      print(t)    #repeated groups gets included even if items are in different order, #used to check the actions of the users in any order as security matter
for t in permutations('Love',2):  #taken 2 at a time
      print(t)
for t in combinations('Love',2):  #repeated group does not get included even if items are in different order
      print(t)

# $Tools
# $Web scraping
# $Python Requests : (to handle sessions and make HTTP requests) and
# $Beautiful Soup (for parsing the response and navigating through it to extract info) to be perfect pair.We used requests to get the page from the AllSides server, but now we need the BeautifulSoup library (pip install beautifulsoup4) to parse HTML and XML. When we pass our HTML to the BeautifulSoup constructor we get an object in return that we can then navigate like the original tree structure of the DOM.
# $Scrapy : For bigger scraping projects (where I have to collect and process a lot of data and deal with non-JS related complexities)
# $Selenium : For JavaScript-heavy sites (or sites that seem too complex)

# $Let's write a simple Python function to get this value. We'll use BeautifulSoup for parsing the HTML.
# $data from :  Socialblade's Real-time Youtube Subscriber Count Page
# $From visual inspection, we find that the subscriber count is inside a <p> tag with ID 'rawCount'
# $'BeautifulSoup' for parsing the HTML.
# $Getting html content as a string
import requests

url = 'https://www.learndatasci.com/tutorials'
r = requests.get(url)
data = str(r.content[:100])
print(f'First 100 code characters from any website : {data}')

# $Beautiful soup example
# $Request and response
from bs4 import BeautifulSoup
r = requests.get('https://www.allsides.com/media-bias/media-bias-ratings')
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

# $Get all table rows
row = rows[0]
print("\n\n\n\nRow : ",row)

# $Retriving the data
print("\nRetriving the data")
# $Get <td> element of '.source-title' class and get the text part from it
name = row.select_one('.source-title').text.strip() #.text gets all the text from the code(not the actual html code)
print("\nName (td) : ",name)

# Get the same '.source-title' 'text' html link
allsides_page = row.select_one('.source-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page
print("It's html url : ",allsides_page)

# $Get another 'td's 'image' html link
bias = row.select_one('.views-field-field-bias-image a')['href']
print("Bias Image link : ",bias)
bias = bias.split('/')[-1]
print("Bias Image end loc(inside server) : ",bias)

# $Get another 'td's agree/disagree count
agree = row.select_one('.agree').text
agree = int(agree)
disagree = row.select_one('.disagree').text
disagree = int(disagree)
print(f"Agree: {agree}, Disagree: {disagree}")

# $It shows up as None because this element is rendered with Javascript and requests can't pull HTML rendered with Javascript
print("Can't show content rendered with javascript : ",row.select_one('.community-feedback-rating-page'))

# $So is there other way to get that info??
# $To find the JS files they're using, just CTRL+F for ".js" in the page source and open the files in a new tab to look for that logic.
# $It turned out the logic was located in the eleventh JS file and they have a function that calculates the text and color with normal switch case taking 'agree_ratio' as the parameter. Now we can write a function to replicate that same logic since we have the ratio
agree_ratio = agree / disagree
def get_agreeance_text(ratio):
    if ratio > 3: return "absolutely agrees"
    elif 2 < ratio <= 3: return "strongly agrees"
    elif 1.5 < ratio <= 2: return "agrees"
    elif 1 < ratio <= 1.5: return "somewhat agrees"
    elif ratio == 1: return "neutral"
    elif 0.67 < ratio < 1: return "somewhat disagrees"
    elif 0.5 < ratio <= 0.67: return "disagrees"
    elif 0.33 < ratio <= 0.5: return "strongly disagrees"
    elif ratio <= 0.33: return "absolutely disagrees"
    else: return None
    
print("Community (got via .js file) : ",get_agreeance_text(agree_ratio))


# $Now let's get all the data into a dictionary in list
data= []

for row in rows:
    d = dict()
    
    d['name'] = row.select_one('.source-title').text.strip()
    d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.source-title a')['href']
    d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
    d['agree'] = int(row.select_one('.agree').text)
    d['disagree'] = int(row.select_one('.disagree').text)
    d['agree_ratio'] = d['agree'] / d['disagree']
    d['agreeance_text'] = get_agreeance_text(d['agree_ratio'])
    
    data.append(d)

print("\n\n\nData:")
print(data[0])  

# $Now let's get all data from all 3 pages simpultaneously
pages = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
    'https://www.allsides.com/media-bias/media-bias-ratings?page=1'
]

# $According to AllSides' robots.txt we need to make sure we wait ten seconds before each request.Our loop will:
#$    request a page
#$    parse the page
#$    wait ten seconds
#$    repeat for next page.

from time import sleep

all_data= []
i=0
for page in pages:
    print("\n\nIter : ",i)
    i+=1
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        d['name'] = row.select_one('.source-title').text.strip()
        d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.source-title a')['href']
        d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
        d['agree'] = int(row.select_one('.agree').text)
        d['disagree'] = int(row.select_one('.disagree').text)
        d['agree_ratio'] = d['agree'] / d['disagree']
        d['agreeance_text'] = get_agreeance_text(d['agree_ratio'])

        all_data.append(d)
    
    sleep(10)

print("\nAll data length :", len(all_data))

# $Store and retrive data to/from local disk file
import json
with open('allsides.json', 'w') as f:
    json.dump(all_data, f)

with open('allsides.json', 'r') as f:
    data2 = json.load(f)

# $Visualising data(dictionary) with pandas
import pandas as pd

df = pd.read_json(open('allsides.json', 'r'))
df.set_index('name', inplace=True)
df.head()

df[df['agreeance_text'] == 'strongly disagrees']

# $Error handeling
while True:
  try:
    age = input("\nEnter your age : ")
    print(int(age))
  except ValueError :
    print("Please enter a number!")
    continue
  except TypeError :
    print("Please enter a correct type!")  
    continue
  else:
    print("Thank you !")
    break    
  finally:
    print("Ok, i'm done here")


def sum(num1, num2):
  try:
    return num1+num2
  except (TypeError,ZeroDivisionError) as err:
    print("\nProgram error : ",err)

print(sum(1,'2'))  

# $ Assertions
# assertions are just use to verify the values at a given point of time to cross check for debugging, it crashes the program at the point where the assertion fails by adding exception
assert 5+3 == 8   #runs perfectly fine as the assumption 8 is correct
assert 5+3 == 9   #crashes with an 'AssertionError' statement



# $Regular expressions(Search for particulat thing in the text)
import re

string = "this search inside of this text please!"
print(f"Search present : {'search' in string}")

# $Search using pattern
print("\nSearch using pattern")
pattern = re.compile("this")
a = pattern.search(string) #<-returns an 'match' object
print("a : ",a)
print("a start index : ", a.start())
print("a end index : ", a.end())

print("\nFind all instances :", pattern.findall(string))
print("\n Simple match : ",pattern.match(string))
print("\n Full match : ",pattern.fullmatch(string))


# $Email validation
print("\nEmail validation using patterns")
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "plathiya2611@gmail.com"

a = email_pattern.search(email)
print("a : ",a)

# $Password validation
print("\nPassword validation(atleast 8 chars, any letters, numbers, $%#@)")
password_pattern = re.compile(r"[^(a-zA-Z0-9)0-9$%#@)]{8,}]")
password = "Winner"
b = password_pattern.search(password) #<-this for some reason is not working
print("b : ",b)


# $Security Hash functions 
import hashlib

hashlib.md5('The tale of two cities')   #gives encoding error as md5 does not accept string but encoded string
hashlib.md5('The tale of two cities'.encode('utf-8'))   #returns hash object
hashlib.md5('The tale of two cities'.encode('utf-8')).digest()  #the md5 en-coded string
hashlib.md5('The tale of two cities'.encode('utf-8')).hexdigest() #the md5 en-coded string in hex

# hashlib is insecure now, came sha
hashlib.sha1('The tale of two cities'.encode('utf-8'))
hashlib.sha1('The tale of two cities'.encode('utf-8')).digest()
hashlib.sha1('The tale of two cities'.encode('utf-8')).hexdigest()

hashlib.sha256('The tale of two cities'.encode('utf-8')).digest()
hashlib.sha512('The tale of two cities'.encode('utf-8')).digest()

#still not secure with GPU's processing, so we do it multiple times
b = 'The tale of two cities'.encode('utf-8')
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()

#might be efficient, but we have better encryption, i.e., pbkdf2_hmac
#that just makes the slows down the forward password gussing attacks slower
p = 'The tale of two cities'.encode('utf-8')
hashlib.pbkdf2_hmac('sha256',p,b'some company phrase', 10000)
hashlib.pbkdf2_hmac('sha256',p,b'some other phrase', 10000)   #this makes another hash unique to each company

# $Another common  security concern preservation with simple strings reserving the addition of tokens and its style
s = 'the quick'
t = 'brown fox'
s+t     #combining tokens to login in the website

#hacker can know the final string and combine it any ways
s = 'the '
t = 'quick brown fox'
s+t     #since the hacker can also reach the final point from anywhere, security is vulnerable

#quick fix -> make a tuple repr of tokkens
s = 'the quick'
t = 'brown fox'
repr((s,t))

#now if a hacker got all tokkens and tries to combine them to access login
s = 'the '
t = 'quick brown fox'
repr((s,t)) #he obtains a different object from before although he has all the tokens

#///////////////////////////////// Python Basics  ///////////////////////
#////////////////////////////////////////////////////////////////////////

# next file :
# $When we create a package, the __init__.py file es created to let the package know it is a python package
# next file :
import utility
import  shopping.shopping_cart

if __name__ == '__main__':

    print("\nRun this code")
    print(shopping.shopping_cart.buy('apple'))
    
    print("\nDefault name of the file that we run is '", __name__, "'")
    # $That can be seen in the 'type' member function
    class Student():
        pass

    import utility
    print("Type of object", type(utility))     #<- shows this object is in the utility module")

    import random
    print(f'\nRandom : {random.random()}')
    print(f'Random Int(between) : {random.randint(1,10)}')
    my_list = [1,2,3,4,5]
    print(f'Random choice: {random.choice(my_list)}')
    random.shuffle(my_list)
    print("Shuffled list : ", my_list)


# next file :
# $Utility functions
def sum(*args):
    sum=0
    for item in args:
        sum+=item
    return sum


# next file :
# $Send email using smtp server
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Zacon'
email['to'] = 'plathiya2611@gmail.com'
email['subject'] = "Information about Zacon!"
email.set_content(('I am a python Master'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() #adding encryption
    smtp.login('lucifer26111990@gmail.com', 'Nathikhabar')  #this might not work if two factor authentication is on or if google setting: Allow users to manage their access to less secure apps, not enabled
    smtp.send_message(email)
    print("sent!")


# next file :
# $Working with file i/o

import os
print(os.listdir("./"))       #returns list of directory names only

import glob
print(glob.glob('./*.py'))    #returns all files of type specified but with it's format/path specified in the search string, just replacing the *

print()


my_file = open('text.txt')

# $Analysing the cursor position
print("\nAnalysing the cursor position")
print(my_file.read())
print(my_file.read())   #<-returns nothing as the cursor has moved to the end of the file
print(my_file.read())   #<-returns nothing as the cursor has moved to the end of the file

print("\nRedirecting the cursor position")
my_file = open('text.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())   #<-returns nothing as the cursor has moved to the end of the file

print(my_file.readline())
print(my_file.readline())

my_file.close()

# $standard way to work with files
print("\nAppending the file from the cursor position")
try:
    with open('text.txt',mode="r+") as my_file:
        text = my_file.write("Hey! How you doin...")
        print(text)
        print("Via simple filename :",my_file.read())   #<-this way you don't need to close the file
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Some error while input/output")

# $Default file path from the current working directory example
print("\nGetting the file via 'windows' file syntax using escape character to escape the escape character")
with open(".\\text\\text.txt", mode='r') as my_file2:
    print("Via file path : ",my_file2.read())

# $("..\\text\\text.txt", mode='r') #<-to go back one directory and then search the file


# next file :
# Pythono3 code to rename multiple 
# files in a directory or folder 
import os 

# Function to rename multiple files 
# def main():
#   i=0
#   for filename in os.listdir(os.getcwd):
#     dst =str(i) + ".jpg"
# 	  src =filename
# 	  os.rename(src, dst)
# 	  i += 1
#   print(str(i)) 
	


# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 


# next file :
# Improting Image class from PIL module  
from PIL import Image 
import PIL 
import os
import cv2
  
for i,x in enumerate(os.listdir("../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/dog/")):
    # Opens a image in RGB mode  
    
    # change names
    # xx = str(i)+".jpg"
    # src = "../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/dog/"+x
    # des = "../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/dog/"+xx
    # os.rename(src,des)

    # reshape
    # im = Image.open("../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/"+str(i)+".jpg")  
    image = cv2.imread("../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/dog/"+x, 1) 
    # newsize = (150, 150) 
    resized = cv2.resize(image,(150,150))
    # im = im.resize(250,250, Image.LANCZOS)
    print('Done! ')

    cv2.imwrite("../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/dog/"+x,resized)
    # image.save("../ml/projects/dogs_vs_cats_image_classification/extracted_data/dogs_vs_cats/train/"+str(i)+".jpg")



# next file :
# $use OpenCV for reading and writing files (intermediate:array_form)
import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n12478768'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))