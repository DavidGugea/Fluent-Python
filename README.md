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