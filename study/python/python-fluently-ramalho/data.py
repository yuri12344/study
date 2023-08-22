# 1 DATA MODELING
import collections
import ipdb

from random import choice

# Especial methods, is better dont set special methods in class, because builtin python methods are more fast
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('QJKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks 
                                        for suit in self.suits]

    # I can print len of the cards
    def __len__(self):
        return len(self._cards)

    # Get item turns class iterable - can take one or iterate over all
    # if I dont use it, when I call choice(deck) I will got, obj is not subscriptable error
    def __getitem__(self, position):
        return self._cards[position]

    # Just a better print
    def __str__(self):
        return "".join(f'Card: {item.rank} {item.suit}. ' for item in self._cards)

deck = FrenchDeck()
len(deck) # 52

choice(deck) # Get random card - Its is only possible because we have __getitem__ in class

for card in deck: # Because i have __getitem__ in my class, my deck are iterable
    # print(card)
    ...
"""
Card(rank='2', suit='spades')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='clubs')
Card(rank='2', suit='hearts')...
"""

for card in reversed(deck): 
    # print(card)
    ...
"""
Card(rank='A', suit='hearts')
Card(rank='A', suit='clubs')
Card(rank='A', suit='diamonds')
Card(rank='A', suit='spades') ...
"""

# The iteration is implicity, if i dont have method contains, the operator will do a sequencial sweep
# in our case, will work, because deck is iterable because the __getitem__
Card('Q', 'hearts') in deck  # True
Card('20', 'beasts') in deck  # False

# Rank and ordenation
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Ordenate the cards, will show the higher to lower, starting by rank 2 and suits clubs
for card in sorted(deck, key=spades_high):
    # print(card)
    ...

"""
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
Card(rank='2', suit='spades')...
"""



# 2 EMULATING NUMERIC TYPES
from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Shows Vector(int, int), instead will show <Vector object at 0x10e10070>
    # Not ambiguous, for understeand the obj creation. Take care with infinit looping with reference yourself
    # Reference: https://bit.ly/36zWl87 Stack Overflow
    def __repr__(self) -> str:
        return f'Vector{self.x, self.y}' 
        # return 'Vector(%r, %r)' % (self.x, self.y)

    # def __str__(self) -> str:
    #    return f'Vector{self.x, self.y}' 
    
    def __abs__(self):
        return hypot(self.x, self.y)

    # add and mul returns new object
    # we can operate numbers, but not Vectors for numbers
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    # Returns a new Vector, not the same object, first value not change
    # Page 78 
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # I can define when my class is True or Not
    # Any obj in python is accept in bool context, Python applyes bool(x) which aways returns True or False
    # by default, Python will call x.__len__() if __bool__ is not implemented
    def __bool__(self):
        # return False - Aways will return False
        # return True - Aways will return True
        return bool(abs(self))

v1 = Vector(2, 4)
v2 = Vector(2, 1)
res = v1 + v2 # 4, 5

v = Vector(3, 4)
abs(v) # 5



# 3 DATA STRUCTURING
""""
- Sequence container
list, tuple and collections.deque 
can store different types of objects

- Simple sequence
str, bytes, bytearray, memoryview and array.array can store only one type

The sequence container store the reference of the objects who have, can be any type
while simple sequence store fisicaly the value of each item in their own space of memory
and not like distinct object.

This way, the simple sequence are more compact, although they are limited to the storage of the
primitive values, like character, bytes and numbers. 

Sample of creating a list and with list compreheension, who can be more fast, and more legible
"""

# ord builting function show's the number of the simbol in Unicode table https://bit.ly/3t5ww7k
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
# [36, 162, 163, 165, 8364, 164] Tip: the break lines in python are ignored betwen the pairs [], {} and (), you dont need to use \

""""
In python 2.x, variable in listcomps can leak

x = 'my precious'
dummy = [x for x in 'ABC']
print(x) 
'C'

Now in python 3.x, the variable x is not leaked
"""

# Comparing list comprehension and with map and filter
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

# timeit.repeat arg setup can receive string and will try compile it
def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

"""
clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

listcomp        : 0.010 0.010 0.011 0.010 0.011
listcomp + func : 0.017 0.016 0.017 0.017 0.017
filter + lambda : 0.015 0.015 0.014 0.015 0.014
filter + func   : 0.024 0.014 0.014 0.014 0.013
"""

# Cartesian product, the product of all possible combinations of the elements of two sequences
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors # Colors first
                         for size in sizes ] # Sizes second
# List of tshirts ordenated by color, then by size
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

# Usage of genexp
import array
symbols = '#!@#!@%*'
res = tuple(ord(symbols) for symbols in symbols)
# print(res) 
# (35, 33, 64, 35, 33, 64, 37, 42)

res = array.array('I', (ord(symbols) for symbols in symbols))
# print(res) 
# array('I', [35, 33, 64, 35, 33, 64, 37, 42])

# Print all possible of Tshirts
# [print(color, size) for color in colors for size in sizes] 
"""
black S
black M
black L
white S
white M
white L
"""

travelers_id = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# The %s/%s understand the tuple, and will print the first and second elemente
# [print('%s/%s' % passp) for passp in sorted(travelers_id)] 
"""
BRA/CE342567
ESP/XDA205856
USA/31195855
"""

# Unpacking, the _ variable is most used to ignore the value
# [print(country) for country, _ in sorted(travelers_id)] 
"""
BRA
ESP
USA
"""

import os
_, filename = os.path.split('/home/user/test.txt')
# print(filename) # test.txt  

a, b, * rest = range(5)
# print(a, b, rest) # 0 1 [2, 3, 4]

a, *rest, b = range(20)
# print(a, rest, b) # 0 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 19

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

# print('{:15} | {:9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        # print(fmt.format(name, latitude, longitude))
        ...
"""
Only occidental hemisphere area
                | lat.      |   long.  
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
Sao Paulo       |  -23.5478 |  -46.6358

All areas
                | lat.      |   long.  
Tokyo           |   35.6897 |  139.6917
Delhi NCR       |   28.6139 |   77.2089
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
Sao Paulo       |  -23.5478 |  -46.6358
"""

# Named tuples
from collections import namedtuple

# Like instance of class, i need a name and a list of iterable attributesm can be str separated by spaces
City = namedtuple('City', 'name country population coordinates') 

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) # City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

#I can acces the values by the name or position
tokyo.population # 36.933
tokyo.coordinates # (35.689722, 139.691667)
tokyo[1] # 'JP'

# namedtuple have more attributes than a tuple, _fields and _make(iter) and instance method _asdict()

City._fields # ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.953, LatLong(28.613889, 77.208889)) # ('Delhi NCR', 'IN', 21.953, LatLong(lat=28.613889, long=77.208889))
delhi = City._make(delhi_data) # City(name='Delhi NCR', country='IN', population=21.953, coordinates=LatLong(lat=28.613889, long=77.208889))
delhi._asdict() # {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.953, 'coordinates': LatLong(lat=28.613889, long=77.208889)}

"""
_field is one tuple with the fields names of the namedtuple
_make() permits instanciate the one namedtuple by the one iterable City(*delhi_data) do the same
_asdict() return a OrderedDict with the namedtuple values
"""

# Tuple and list methods 

# s.__add__ or + "Concatenation" Can be used in LISTS and TUPLES
tuple_0 = (1,)
tuple_1 = tuple_0.__add__((2,)) # (1,2) - Or tuple_1 = tuple_0 + (2,)

list_0 = [1]
list_1 = list_0.__add__([2]) # [1,2] - Or list_1 = list_0 + [2]

# s.__iadd__ or += "Concatenation in place" can only be used in LISTS
list_0 = [1]
list_1 = list_0.__iadd__([2]) # [1,2] - Or list_1 = list_0 += [2]

# s.apped(e) "Concatenate after last element" can only be used in LIST
list_1.append('Hi') # [1,2,'Hi']

# s.clear() "Clear the list" can only be used in LIST
list_1.clear() # []

# s.__contains__(e) "Check if element is in the list" can be used in LIST and TUPLE
list_1.__contains__(1) # True or False if dont have
tuple_1.__contains__(1) # True or False if dont have

# s.copy() "Shallow Copy the list"
shallow_list = list_1.copy() # [1,2]

# s.count(e) "Count the number of elements" can be used in LIST and TUPLE
list_1.count(1) # 1
tuple_1.count(1) # 1

# s.__delitem__(pos) "Delete element by position" can only be used in LIST
list_1 = [1,2,3]
del list_1[0] # [2, 3]
list_1.__delitem__(0) # [3]

# s.extend(it) "Extend the list by iterable" can only be used in LIST
list_1, list_2 = ([1,2,3], [4,5,6])
list_1.extend(list_2) # [1,2,3,4,5,6] - Doest not return new list, but list_1 have the new values

# s.__getitem__(pos) "Get element by position" can be used in LIST and TUPLE
list_1.__getitem__(0) # Position is 0, so will return 1

# s.__getnewargs__() "Is used in obj serialization with pickle" can only be used in TUPLE
# import pickle
class Abcd(object):
  def __new__(cls, *args):
    print("In A::__new__(%s, args=%s)" % (cls, args)) 
    return super(Abcd, cls).__new__(cls)

  def __init__(self, x, y):
    print("In A::__init__(%s, %s, %s)" % (self, x, y)) 
    self.x, self.y = x, y

  def __getnewargs__(self):
    print("In A::__getnewargs__(%s):" % (self,)) # Its called when you call byte_data = pickle.dumps(obj)
    return (self.x, self.y)

  def __setstate__(self, state):
    print("In A::__setstate__(%s, %s):" % (self, state)) 
    # Note:  Called in the case of unpickling, when the class is being constructed.
    # super(A, self).__setstate__(state)
    self.__dict__.update(state)

"""
    For this code work, you need to create new Python file
    
    from data import Abcd
    import pickle
    
    abc = Abcd(2,3) # __init__ and __new__ are called
    byte_data = pickle.dumps(abc) # Bytes code /  __getnewargs__ is called
    
    # Now you can use the byte_data to transport above the internet
   
    a2 = pickle.loads(byte_data) # __setstate__ is called, unpacking the data
    
    # now abc and a2 are same obj
    # bytedata
    b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x04data\x94\x8c\x04Abcd\x94\x93\x94K\x02K\x03\x86\x94\x81\x94}\x94(\x8c\x01x\x94K\x02\x8c\x01y\x94K\x03ub.
"""

# s.index(e) "Return the index of the first element" can be used in LIST and TUPLES
tuple_list = (1,2,3,4,5) # Same for lists
tuple_list.index(3) # 2

# s.insert(pos, e) "Insert element at position" can only be used in LIST
list_1 = [1,2,3]
list_1.insert(0, 0) # [0,1,2,3]

# s.__iter__() "Return an iterator object" can be used in LIST and TUPLE
list_iterator = list_1.__iter__() # <list_iterator object at 0x7f8b8b8b8d10>

# s.__len__() "Return the length of the list" can be used in LIST and TUPLE
list_1.__len__() # 3

# s.__mul__(n) "Return new list concatenating x times" can be used in LIST and TUPLE
list_1 = ["Abc"]
list_2 = list_1.__mul__(2) # list_1 = ["Abc"] | list_2 = ["Abc", "Abc"]

tuple_1 = ('Abc')
tuple_2 = tuple_1.__mul__(2) # tuple_2 = ('AbcAbc')

tuple_1 = ('Abc', 'Cba')
tuple_2 = tuple_1.__mul__(2) # tuple_2 = ('Abc', 'Cba', 'Abc', 'Cba')

# s.__imul__(n) " s * n | Return new LIST or TUPLE Repeat concatenation in place"
list_1 = ["Abc", "Cba"]
list_2 = list_1.__imul__(5) # list_2 = ['Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba']

# s.__rmul__(n) " n * s | reversed | Return new list OR TUPLE Repeat concatenation, "
list_1 = ["Abc", "Cba"]
list_2 = list_1.__rmul__(5) # list_2 = ['Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba', 'Abc', 'Cba']

# s.pop(pos) "Remove and return element at position or the last without argument" can only be used in LIST
list_1 = ["First", "Second", "Last"]
last = list_1.pop() # Return value and remove from the list # "Last"
first = list_1.pop(0) # Return value and remove from the list # "First"

# s.remove(e) "Dont return nothing, remove the first element in the LIST"
list_1 = ["First", "Second", "Last"]
list_1.remove("First") # ["Second", "Last"] # Remove the first element and dont have return value

# s.reverse() "Dont have return, Reverse the list in place"
list_1 = ["First", "Second", "Last"]
list_1.reverse() # ["Last", "Second", "First"]

# s.__reversed__() "Return a reverse iterator of the LIST"
list_1 = ["First", "Second", "Last"]
list_1_reverse_iterator = list_1.__reversed__() # <list_iterator object at 0x7f8b8b8b8d10>

for item_reversed in list_1_reverse_iterator:
  # print(item_reversed) # Last, Second, First
  ...

# s.__setitem__(pos, e) "Dont have return, Set element at position, overwriting the existing one" can only be used in LIST
list_1 = ["First", "Second", "Last"]
list_1.__setitem__(0, "First_new") # ["First_new", "Second", "Last"]

# s.sort() "Sort values in-place, Dont have return" - Optional arguments ([key], [reverse])
list_1 = [5, 2, 1, 9, 5, 10, 5, 9, 7, 2, 146, 7, 10, 15]

list_1.sort() # [1, 2, 2, 5, 5, 5, 7, 7, 9, 9, 10, 10, 15, 146]
list_1.sort(reverse=True) # [146, 15, 10, 10, 9, 9, 7, 7, 5, 5, 5, 2, 2, 1]

def odd_numbers_first(item):
    return item % 2 == 1

list_1.sort(key=odd_numbers_first, reverse=True) # [15, 9, 9, 7, 7, 5, 5, 5, 1, 146, 10, 10, 2, 2]



# Slicing
# Why RANGE and SLICE aways cut's the last element?
# Its more easy to understand, and calculate the len
# In this case, 10 - 20, the len will be 10, and numbers will be 10 until 19 (not 20)

list_1 = [x for x in range(10,20)] # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] - 10 lenght - Cuts the 20

# And is easy to separate the elements without overlaping by the indice
half_list_1 = list_1[:5] # [10, 11, 12, 13, 14] - Starts at indice 0 until Indice 5, cuts the 15 | Numbers 10 - 14
half_list_2 = list_1[5:] # [15, 16, 17, 18, 19] - Starting in 5 indice, come until the end | Numbers 15 - 19

large_text = "This os a very large text"
large_text[::5] # "Tovl" Print the characters, steping 5 steps in this case, aways cutting the last element

                 # "text large very a os this" <- reverse TEXT to compare
large_text[::-1] # "txet egral yrev a so sihT" <- result of the reverse CHARACTERS - reversing character by character
                 # Start in the last character and put him as the first

large_text = "This is a very large text and great tecnology we are doing here"

splited_words = large_text.split() # ['This', 'is', 'a', 'very', 'large', 'text', 'and', 'great', 'tecnology', 'we', 'are', 'doing', 'here']

splited_words[0::1] # ['This', 'is', 'a', 'very', 'large', 'text', 'and', 'great', 'tecnology', 'we', 'are', 'doing', 'here']
# No jumping because 0::1 is the same as 0::, because you aways cut the last, so 1 - 1 = 0, so jump 0, no jumping
# [::] doble : means steps soo, [0::1] means start in 0, and jump 0 (no jumpings)

splited_words[0::2] # ['This', 'a', 'large', 'and', 'tecnology', 'are', 'here']
# [0::2] means start in 0, and jump 1 because slice and range aways cut the last
# Starting by 0 and jumping one word everytime



invoice = """
0.....6..............................40..........55.....55.......... 
1909  Pimoroni PiBrella             $17.50    3    $52.50
1489  6mm Tactile Switch x20         $4.95    2     $9.90
1510  Panavise Jr. - PV-201          $28.00    1    $28.00
"""

DESCRIPTION = slice(6,35)
UNIT_PRICE = slice(38,45)
line_items = invoice.split('\n')[2:] # Skips the 2 first \n First is before """ and second is before the First line
for item in line_items:
    # print(item[UNIT_PRICE], item[DESCRIPTION])
    ...
"""
7.50    Pimoroni PiBrella            
4.95    6mm Tactile Switch x20       
28.00   Panavise Jr. - PV-201 
"""
# Who treat the Slices in Python is __getitem__ and __setitem__


# Value atributing to slices
list1 = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Right side need to me iterable, or you will be get a error
list1[2:5] = [20, 30, 30, 30, 30] # [0, 1, 20, 30, 30, 30, 30, 5, 6, 7, 8, 9]
# Extras values will add to the list, but same values in the indice will be overwritten
# And less values will be removed from the list

# Using + and * with sequences, aways return new obj, and dont modify the original
list1 = [1,2,3]
list2 = list1 * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
five_a = 5 * 'a' # 'aaaaa'

# Wrong way to do it
board = [['_'] * 3 ] * 3 # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 0 # [['_', '_', 0], ['_', '_', 0], ['_', '_', 0]]


# Right way to do it
board = [['_'] * 3 for i in range(3)]
board[1][2] = 0 # [['_', '_', '_'], ['_', '_', 0], ['_', '_', '_']]



"""
Wrong Way explanation

This happens because the list is a reference to the same object
behavior like code above:

row = ['_'] * 3 # Same reference
board = []
for i in range(3):
    board.appaned(row)

aways concateneting same row reference


Right Way explanation
behavior like code above:

board = []
for i in range(3):
    row = ['_'] * 3 # New reference
    board.append(row)

each interation create new row and concat with board
"""


# Combined attribution and sequences

# Mutable sequences
l = [1,2,3]
id(l) # 140361155724736

l *= 2 # [1, 2, 3, 1, 2, 3]
id(l) # 140361155724736 - Same object with new itens

# Imutable sequence
t = (1,2,3)
id(t) # 139999474455424
t *= 2 # (1, 2, 3, 1, 2, 3)
id(t) # 139864951363168 != 139999474455424

# The enigma about attribuition

t = (1,2, [30,40])
# t[2] += [50,60]

# TypeError: 'tuple' object does not support item assignment
# (1, 2, [30, 40, 50, 60])
import dis
# dis.dis('tuple_here[index_of_list_here] += other_list_here')

"""
  1           0 LOAD_NAME                0 (tuple_here) 
              2 LOAD_NAME                1 (index_of_list_here)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_NAME                2 (other_list_here)
             10 INPLACE_ADD
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
"""

"""
- tuple_here is on the TOS (Top of Stack)
- In 10 - Execute TOS += other_list_here
- It works when TOS refeers to mutable object
- It doesn't work when TOS refeers to imutable object, like in line 572

We can understeand, put mutable object inside a tuple its not a good idea
"""


list1 = [5,6,214,9,5,97,56,148,126,32]

# Inplace, no return, return is None, doenst appear in console
# with no return, we cant chain other methods
# change list in place
list1.sort()

# Return a new list
# doenst change list
list2 = sorted(list1)

import itertools
import heapq  

objects = [
    {"species": "cat", "name": "fluffy"},
    {"species": "cat", "name": "Kid"},
    {"species": "cat", "name": "Boris"},
    {"species": "dog", "name": "Jack"},
    {"species": "dog", "name": "Nina"},
    {"species": "dog", "name": "Mel"},
    {"species": "dog", "name": "Chorao"},
]

iterator_by_species = itertools.groupby(objects, lambda x: x["species"])

res = []
for specie, names in iterator_by_species:
    res.append({ specie: [name['name'] for name in names] })

res # [{'cat': ['fluffy', 'Kid', 'Boris']}, {'dog': ['Jack', 'Nina', 'Mel', 'Chorao']}]

# Taking the 3 largest numbers
res = heapq.nlargest(3, list1) # [148, 126, 214]


# Binary search testing left and right
from bisect import bisect_left

list1 = [5, 5, 6, 9, 32, 56, 97, 56, 97, 56, 97, 56, 97, 126, 148, 214]
list1.sort()

ltr = bisect_left(list1, 32) # 4
list1[ltr] # 32


HAYSTACK = [1, 4, 5, 6, 8, 11, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:3d} {2}{0:2d}'

def demo(bisect_left):
    for needle in reversed(NEEDLES):
        position = bisect_left(HAYSTACK, needle)
        offset = position * '  |'
        #print(ROW_FMT.format(needle, position, offset))

# print('DEMO:', bisect_left.__name__)
# print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_left)

"""
DEMO: bisect_left
haystack ->  1  4  5  6  8 11 12 15 20 21 23 23 26 29 30
31 @  15   |  |  |  |  |  |  |  |  |  |  |  |  |  |  |31
30 @  14   |  |  |  |  |  |  |  |  |  |  |  |  |  |30
29 @  13   |  |  |  |  |  |  |  |  |  |  |  |  |29
23 @  10   |  |  |  |  |  |  |  |  |  |23
22 @  10   |  |  |  |  |  |  |  |  |  |22
10 @   5   |  |  |  |  |10
 8 @   4   |  |  |  | 8
 5 @   2   |  | 5
 2 @   1   | 2
 1 @   0  1
 0 @   0  0
"""

import random
import bisect

def grade(score, breakpoints=[50,60,70,80,90,100], grade=['I', 'S', 'B', 'E', 'O']):
    if score < 50: 
        return 'I'
    a = bisect_left(breakpoints, score)
    return grade[a-1]

students_results = [random.randint(0, 10) * 10 for _ in range(10)]
res = [grade(number) for number in students_results] # ['B', 'O', 'I', 'O', 'I', 'E', 'I', 'I', 'E', 'I']

my_list = []
for i in range(20):
    new_item = random.randrange(20*2)
    bisect.insort(my_list, new_item) # Insert items in order
    # print('%2d ->' % new_item, my_list)
"""
26 -> [26]
 3 -> [3, 26]
 7 -> [3, 7, 26]
22 -> [3, 7, 22, 26]
21 -> [3, 7, 21, 22, 26]
 1 -> [1, 3, 7, 21, 22, 26]
 8 -> [1, 3, 7, 8, 21, 22, 26]
 0 -> [0, 1, 3, 7, 8, 21, 22, 26]
15 -> [0, 1, 3, 7, 8, 15, 21, 22, 26]
34 -> [0, 1, 3, 7, 8, 15, 21, 22, 26, 34]
18 -> [0, 1, 3, 7, 8, 15, 18, 21, 22, 26, 34]
 7 -> [0, 1, 3, 7, 7, 8, 15, 18, 21, 22, 26, 34]
10 -> [0, 1, 3, 7, 7, 8, 10, 15, 18, 21, 22, 26, 34]
17 -> [0, 1, 3, 7, 7, 8, 10, 15, 17, 18, 21, 22, 26, 34]
17 -> [0, 1, 3, 7, 7, 8, 10, 15, 17, 17, 18, 21, 22, 26, 34]
18 -> [0, 1, 3, 7, 7, 8, 10, 15, 17, 17, 18, 18, 21, 22, 26, 34]
39 -> [0, 1, 3, 7, 7, 8, 10, 15, 17, 17, 18, 18, 21, 22, 26, 34, 39]
 5 -> [0, 1, 3, 5, 7, 7, 8, 10, 15, 17, 17, 18, 18, 21, 22, 26, 34, 39]
 9 -> [0, 1, 3, 5, 7, 7, 8, 9, 10, 15, 17, 17, 18, 18, 21, 22, 26, 34, 39]
14 -> [0, 1, 3, 5, 7, 7, 8, 9, 10, 14, 15, 17, 17, 18, 18, 21, 22, 26, 34, 39]
"""


# Arrays 
from array import array
import sys

# floats = [random.random() for number in range(10**7)]
# print(sys.getsizeof(floats)) # 89.095.160 bytes or 89 mb

floats = array('d', ( random.random() for i in range(10**7) ) )
# print(sys.getsizeof(floats)) # 81.940.368 bytes or 81mb
print(floats[:-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close() 
print(floats2[:-1])

floats2 == floats # True

"""
STEPS:
- import type array
- Create one array with floating point
- Inspect last element
- Create a empty double array
- Read 10MM binary numbers from file
- Inspect last element
- Verify if they are equal
"""