# Fluent Python by Luciano Ramalho

---

## Part I  - Prologue
## 1. The Python Data Model

---

## Part II - Data Structures
## 2. An Array of Sequences
## 3. Dictionaries and Sets
## 4. Text versus Bytes

---

## Part III - Functions as Objects
## 5. First-Class Functions
## 6. Design Patterns with First-Class Functions
## 7. Function Decorators and Closures

---

## Part IV - Object-Oriented Idioms
## 8. Object References, Mutability and Recycling
## 9. A Pythonic Object
## 10. Sequence Hacking, Hashing, and Slicing
## 11. Interfaces: From Protocols to ABCs
## 12. Inheritance: For Good or For Worse
## 13. Operator Overloading: Doing It Right

---

## Part V - Control Flow
## 14. Iterables, Iterators, and Generators
## 15. Context Managers and else Blocks
## 16. Coroutines
## 17. Concurrency with Futures
## 18. Concurrency with asyncio

---

## Part VI - Metaprogramming
## 19. Dynamic Attributes and Properties
## 20. Attribute Descriptors
## 21. Class Metaprogramming

---

# Part II - Data Structures

---

# 2. An Array of Sequences

## Overview of Built-In Sequences

There are 2 types of sequences:

* *Container sequences*: ```list```, ```tuple``` and ```collections.deque``` can hold items of different types.
* *Flat sequences*: ```str```, ```bytes```, ```bytearray```, ```memoryview``` and ```array.array``` hold items of one type.

*Container sequences* hold references to the objects that they contain while *flat sequences* simply just physically store the value of each item within its own memory.
*Flat sequences* are more compact but they can only hold primitive values.

Another way of grouping sequence types is by mutability:

* *Mutable sequences*: ```list```, ```bytearray```, ```array.array```, ```collections.deque``` and ```memoryview```
* *Immutable sequences*: ```tuple```, ```str``` and ```bytes```

## List Comprehensions and Generator Expressions

### List comprehensions

You can refer to list comprehensions as *listcomps* and generator expressions as *genexps*.

List comprehensions are a quick way of building a list. It's a much more quicker and readable way of building lists than using a classic for-loop.

Here is an example:

```Python
>>> even_numbers_to_100 = [x for x in range(101) if x % 2 == 0]
[0, 2, ..., 100]
```

List comprehensions, generator expressions and set & dict comprehensions have their own scope, just like functions.

Listcomps are also a lot easier to read when it comes to multiple loops.
Here is an example of the cartesian product using listcomps:

```Python
colors = ['black', 'white]
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
"""
Output:

[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
"""
```

### Generator expressions

The difference between generator expressions and other types of comprehensions ( list, set or dict ) is that they are a lot faster since they only use generators. They don't build actual data structure inside the memory which makes them a lot faster but the only thing that you can do is iterate over its items, you can't manipulate the data inside of it.

> To initialize tuples, arrays and other types of sequences, you could also start from a listcomp, but a genexp saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.
> Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.

Example of genexps:

```Python
(x for x in range(10**10+1) if x % 2 == 0)
```

This is a generator expression that built a generator with all the even numbers from 0 to 10**10. It looks a lot like a list comprehension but the difference is that it uses parentheses rather than brackets, as specified earlier.

It is also a lot faster. If you would try to execute the same comprehension but transform the genexp into a listcomp, it would have taken a lot longer since you would have been creating a whole new object inside the memory but the genexp only builds a generator.

Genexps are also widely used when working with files.

## Tuples as Records

Tuples can be used as immutable lists but also as records.
Each item in a tuple can hold data for one field meaning that you can assign specific values to specific fields and store them inside the tuple as a record.

> Tuples hold records: each item in the tuple holds the data for one field and the position of the item gives its meaning
> If you think of a tuple just as an immutable list, the quantity and the order of the items may or may not be important, depending on the context. But when using a tuple as a collection of fields, the number of items is often fixed and their order is always vital

## Tuple Unpacking

Tuple unpacking is used to unpack values from a tuple in specific variables.

> The most visible form of tuple unpacking is **parallel assignment**; that is, assigning items from an iterable to a tuple of variables, as you can see in this example:

```Python
>>> coordinates = (33.9425, -118.408056)
>>> latitude, longitude = coordinates # tuple unpacking
>>> latitude
33.9425
>>> longitude
-118.408056
```

If you don't care about a variable that is getting unpacked from a tuple you can give it the name ```_```:

```Python
>>> coordinates = (33.9425, -118.408056)
>>> _ , longitude = coordinates # tuple unpacking -> you only care about longitude
```

### Using ```*``` to grab excess items

When you are unpacking a tuple and there are a lot of values that you want to store into one single variable you can use the ```*``` operator.

> Defining function parameters with ```*args``` to grab arbitrary excess arguments is a classic Python feature.


```Python
>>> a, b, *rest = range(11)
>>> a
0
>>> b
1
>>> rest
[2, 3, 4, 5, 6, 7, 8, 9, 10]
```

> In the onctext of parallel assignment, the ```*``` prefix can be applied to exactly one variable, but it can appear in any position:

You can also use in the middle of unpacking:

```Python
>>> a, *rest, b = range(11)
>>> a
0
>>> b 
10
>>> rest
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Named Tuples

You can use named tuples to assign certain names to tuple fields and to directly grab their values using those specific names.

> Instances of a class that you build with ```namedtuple``` take exactly the same amount of memory as tuples because the field names are stored in the class. They use less memory than a regular object because they don't store attributes in a per-instance ```__dict__```.

## Tuples as Immutable Lists

The ```tuple``` supports all list methods that doesn't involve changing the data from within the data structure.

|Method|List|Tuple|Short description|
|------|----|-----|-----------------|
|```s.__add__(s2)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```s + s2``` - concatenation|
|```s.__iadd__(s2)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |```s += s2``` - in-place concatenation|
|```s.append(e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |Append one element after last|
|```s.clear()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |Delete all items|
|```s.__contains__(e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```e in s```|
|```s.copy()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |Shallow copy of the list|
|```s.count(e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|Count occurrences of an element|
|```s.__delitem__(p)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |Remove item at position ```p```|
|```s.extend(it)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)| |Append items from the iterable ```it```|
|```s.__getitem__(p)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```s[p]``` - get item at position|
|```s.__getnewargs__()```||![Check Sign](ScreenshotsForNotes/CheckSign.svg)|Support for optimized serialization with ```pickle```|
|```s.index(e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|Find position of first occurrence of e|
|```s.insert(p, e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Insert element ```e``` before the item at position ```p```|
|```s.__iter__()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|Get iterator|
|```s.__len__()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```len(s)``` - number of items|
|```s.__mul__(n)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```s * n``` - repeated concatenation|
|```s.__imul__(n)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||```s *= n``` - in-place repeated concatenation|
|```s.__rmul__(n)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|![Check Sign](ScreenshotsForNotes/CheckSign.svg)|```n * s``` - reversed repeated concatenation|
|```s.pop([p])```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Remove and return last item or item at optional position ```p```|
|```s.remove(e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Remove first occurrence of element ```e``` by value|
|```s.reverse()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Reverse the order of the items in place|
|```s.__reversed__()```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Get iterator to scna item from last to first|
|```s.__setitem__(p, e)```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||```s[p] = e``` - put ```e``` in position ```p```, overwriting existing items|
|```s.sort([key], [reverse])```|![Check Sign](ScreenshotsForNotes/CheckSign.svg)||Sort items in place with optional keyword arguments ```key``` and ```reverse```|

## Building Lists of Lists

When you are building a list of lists, especially using listcomps then you must pay atetntion and not use the same reference to the same list object.

Example of a tic tac toe 'board' done right:

```Python
>>> board = [['_'] * 3 for i in range(3)]
>>> board
>>> [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
>>> board[1][2] = 'X'
>>> board
[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
```

You can see that the list has changed the way we wanted it to since every single list is its own object. We don't have multiple equal references inside the list of lists.

The following example will however not behave the way we indent it to:

```Python
>>> board = [['_'] * 3] * 3
>>> board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
>>> board[1][2] = '0'
>>> board
[['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]
```

This happens because we are building multiple lists that reference the same list object inside the heap.
What this actually does is:

```Python
row = ['_'] * 3
board = []
for i in range(3):
    board.appned(row)
```

## Augmented Assignment with Sequences

```>```

The augmented assignment operators ```+=``` and ```*=``` behave very differently depending on the first operand. To simplify the discussion, we will focus on augmented addition first (```+=```), but the concepts also apply to ```*=``` and to other augmented assignment operators.

The special method that makes ```+=``` work is ```__iadd__``` (for "in-place addition"). However, if ```__iadd__``` is not implemented, Python falls back to calling ```__add__```. Consider this simple expression:

```Python
>>> a += b
```

If *a* implements ```__iadd__```, that will be called.. In the case of mutalbe sequences (e.g, ```list```, ```bytearray```, ```array.array``` ), *a* will be changed in place (i.e, the effect will be similar to ```a.extend(b)``` ). However, when *a* does not implement ```__iadd__```, the expression ```a += b``` has the same effect as ```a = a + b```: this expression ```a + b``` is evealuted first, producing a new object, which is then bound to *a*. In other word, the identity of the object bound to *a* may or may not change, depending on the availability of ```__iadd__```. 

In general, for mutable sequences, it is a good bet that ```__iadd__``` is implemented and that ```+=``` happens in place. For immutalbe sequences, clearly there is no way for that to happen.

What i just wrote about ```+=``` also applies to ```*=```, which is implemneted via ```__imul__``.

Here is a demonstration of ```*=``` with a mutable sequence and then an immutable one:

```Python
>>> l = [1, 2, 3]
>>> id(l)
4311953800
>>> l *= 2
>>> l 
[1, 2, 3, 1, 2, 3]
>>> id(l)
4311953800
>>> t = (1, 2, 3)
>>> id(t)
4312681568
>>> t *= 2
>>> id(t)
4301348296
```

Repeated concatenation of immutable sequences is inefficient, becuase instead of just appending new items, the interpreter has to copy the whole target sequence to create a new one with new items concatenated.
```str``` is an exception to this description. Because string biulding with ```+=``` in loops is so common in the wild, CPython is optimized for this use case. ```str``` instances are allocated in memory with room to spare, so that concatenation does not require copying the whole string every time.

## Mutable sequences inside immutable sequences

Let's take a look at the following example:

```Python
t = (1, 2, [30, 40])
t[2] += [50, 60]
```

In this case, you will receive a ```TypeError``` and ```t``` will change to: ````1, 2, [30, 40, 50, 60]```.

You should never have mutable sequences inside immutable sequences since the operators will mess up.

> Augmented assignment is not an atomic operation

If you want to see the bytecode for what's happening under the hood use ```dis.dis()```:

```Python
dis.dis('t[2] += [50, 60]')
```

## list.sort and the sorted Built-In Function

The ```list.sort``` method sorts the items in place. That means that the sequence that you use it on is changed, it doesn't return a new sequence. Because of that, it **returns None**. It is important for methods that do something in place to return None to remind us that they don't return anything.

The ```sorted``` function however, builds a new sorted sequence of the given argument sequence.

> The ```list.sort``` method sorts a list in place - that is, without making a copy. It returns ```None``` to remind us that it changes the target object, and does not create a new list. 
> This is an important Python API convention: functions or methods that change an object in place should return ```None``` to make it clear to the caller that the object itself was chagned, and now new object was created. The same behavior can be seen, for example, in the ```random.shuffle``` function.

> The convention of returning ```None``` to signal in-place changes has a drawback: you cannot cascadde calls to those methods. In contrast, methods that return new objects (e.g, all ```str``` methods) can be cascaded in the fluent interface style.

> In contrast, the built-in function ```sorted``` creates a new list and returns it. In fact, it accepts any iterable object as an argument, including immutable sequences and generators. Regardless of the type of iterable given to ```sorted```, it always returns a newly created list.

Both ```list.sort``` and the ```sorted``` function have two optional keyword arguments:

* ```reverse```: If ```true```, it returns the sorted sequence in reversed order. Defaults to ```False```.
* ```key```: The ```key``` keyword argument is a function that will be applied to each item in the sequence. This can be very helpful for example when you have a sequence of objects and you want to sort them by a specific property.

## Managing Ordered Sequences with bisect

```>```

The ```bisect``` module offers two main functions - ```bisect``` and ```insort``` - that use the ***binary search algorithm*** to quickly find and insert item in any ***sorted sequences***.

### Searching with bisect

```bisect(haystack, needle)``` does a binary search for *needle* in a *haystack* - which must be a sorted sequence - to locate the position where *needle* can be inserted while maintaining *haystack* in ascending order. In other words, all items appearing up to that position are less than or equal to *needle*. You could use the result of ```bisect(haystack, needle)``` as the ```index``` argument to ```haystakc.insert(index, needle)``` - however, using ```insort``` does both steps and is faster.

### Inserting with bisect

Sorting is expensive, so once you have a sorted sequence, it's good to keep it that way. That is why ```bisect.insort``` was created.

You can use the ```bisect.insort(seq, item)``` to insert an ```item``` into a ```sequence``` in ascending order.

## Arrays

If a list only contains numbers, it's better to work with arrays ( ```array.array``` ). They ar emore efficient thatn lists and support all mutable sequence oprations. It also contains some additional methods for fast loading and saving ( e.g. ```.frombytes``` or ```.tofile``` )

> This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character. The following type codes are defined:

Here is the list of typecodes:

![Array type codes](ScreenshotsForNotes/Chapter2/ArrayTypeCodes.PNG)

Whenever you start building an array, you must give it the underlying C type. You can also give it an optional initializer, which has to be an iterable. 

You can use methods like ```.tofile``` to put an entire array into a file ( using machine code ).

```Python
from array import array

with open("arrayfile.bin", "wb") as f:
    x = array('I', range(6))
    x.tofile(f)
```

The array data structure doesn't have the following methods in comparison to ```list```:

* ```clear()```
* ```copy()```
* ```__reversed__()```
* ```sort([key], [reverse])```

## Memory Views

```>```

The built-in ```memoryview``` class is a shared-memory sequence type that lets you handle slices of arrays wihtout copying bytes.

A memoryview is eseentially a generlized NumPy array structure in Python itlsef (without the math). It allows you to share memory between data-structures ( things like PIL images, SQLite databases, NumPy arrays, etc. ) without first copying. This is very important for large data sets.

Using notation similar to the ```array``` module, the ```memoryview.cast``` method lets you change the way multiple bytes are read or written as units without moving bits around ( just like the C ```cast``` operator ). ```memoryview.cast``` returns yet another ```memoryview``` object, alwyas sharing the same memory.

```Python
>>> numbers = array.array('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview(numbers)
>>> len(memv)
5
>>> memv[0]
-2
>>> memv_oct = memv.cast('B')
>>> memv_oct.tolist()
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
>>> memv_oct[5] = 4
>>> numbers
array('h', [-2, -1, 1024, 1, 2])
```