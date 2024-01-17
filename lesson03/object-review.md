# Python Objects Review

## Introduction

This tutorial will review Python objects.

## What is an Object?

If you recall from earlier study, objects are made up of behavior and data. We call these methods and properties:
* properties are the data defined for the object
* methods are the behaviors defined for the object

With a `string`, the characters in the string are the data, and the methods we can uses, like .lower() or .endswith() are the methods.

The definition of an object is specified in a `class`.

## Declaring Classes

Classes are how we specify objects - what they represent, what they can do, and what information they contain. Classes in Python are declared with the `class` keyword. Following the `class` keyword, the class has a name, which is typically capitalized. After that, we have parentheses and the word object, like this: `(object)`. If we declared a class called Square, it would look like this:

```py
class Square(object):
    # definition would go here
    pass
```

If we want to add methods to our class, we declare them like functions in Python; the difference is that they are indented as to be a part of the class. We use the def keyword, the name of the method, then its parameters in parentheses.

**init** is a special Python method that we'll need. It is used to initialize the properties for an object. It's declared as `__init__` - often called "dunder init" (dunder: **d**ouble **under**score). It shouldn't return a value and should only be used to set up the class.

All Python methods start with a `self` parameter. This parameter is used to assign properties to your object. One of the most common errors I run into in my code repeatedly is forgetting to use `self`, so be diligent!

In the following code, we create a `Square` class with a `side` property by setting `self.side` to the parameter. We also use `__init__` to initialize the value for the side. 

```py
class Square(object):

  def __init__(self, side):
    self.side = side


  def get_area(self):
    return self.side * self.side

```

So far, we have two methods - one special method called `__init__`, a regular method called `get_area`, and a single property called `side`. 


## Instantiating Objects

Now that we've defined a really simple object, we can instantiate it, or create a version of it. There are some things that happen automatically here; when you instantiate an object in Python, the `__init__` method is called, and the parameters to the `__init__` method (aside from `self`) are used. For our `Square` class, this means that we'd instantiate it like this:

```py
side_length = 5
my_square = Square(5)
```

If you wanted to call the method, you'd just use a period and the method's name and its parameters (again, not considering `self` which is automatically translated in the way that Python handles objects).

```py
print(my_square.get_area())
```

Now that we have a class, we can instantiate as many objects as we need!


## Why Use Objects?

This seems like a lot of work just to compute the area of a square, right? While this is true, it's simply a demonstration of something we might use objects for. In practice, objects can be a lot more complex.

There are 3 major reasons why we use objects:
1. Code Reuse. 
   * Once you define a `class`, you can use it to instantiate lots of objects for lots of different purposes.
1. Encapsulation
   * This is an important concept that allows us to consolidate our data and behavior within a single entity. As programs get more complex, this becomes more and more useful.
1. Abstraction
   * Abstraction is one of the most powerful capabilities in programming languages and software engineering. This allows you to treat complex code as something much more understandable to humans. Look at the two code snippets below.

**A:**
```py
s = 5
a = 5 * 5
```

**B:**
```py
s = Square(5)
a = s.get_area()
```

While **A** is definitely more terse, it's pretty clear that the _purpose_ of **B** is much more obvious. While they do the same thing, even with this simple example the code is much more understandable.
