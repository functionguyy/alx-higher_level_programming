# 0x06. Python - Classes and Objects

## Learning Objectives 

- Why Python programming is awesome
- What is OOP
- "first-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and information Hiding
- What is a property
- What is the difference between an attribut and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of
a class
- How to bind attributes to objects and classes
- what is the `__dict__` of a class and/or instance of a class and what does it
contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function



## Why Python programming is awesome

In Python, everything is an object. In other words, "everything" is 
treated the same way: functions and methods are just values like 
lists, integers or floats. Each of these are instances of their corresponding 
classes. Classes and objects are the two main aspects of object-oriented
programming or OOP for short.

## What is OOP
OOP stands for Object Oriented Programming. It is way of organizing your
program to combine data and functionality and wrap it inside something called
an object. OOP is one of the most effective approach to writing software. 

There are four major principles of object-oriented programming and they are:
- Encapsulation
- Data Abstraction
- Polymorphism
- Inheritance

The principle of encapsulation and data abstraction will be discussed in this write-up. 

## "first-class everything"

Python's design is based on the "first-class everything" principle. 

The creator of Python, Guido Van Rossum wrote:

> "One of my goals for Python was to make it so that all objects were "first
> class." By this, I meant that I wanted all objects that could be named in the
> language (e.g., integers, strings, functions, classes, modules, methods, and
> so on) to have equal status. That is they can be assigned to variables,
> placed in lists, stored in dictionaries, passed as arguments, and so forth"
> (Blog, The History of Python, February 27, 2009).

So basically everything in Python is an object of a class or,
in the words on Guido, first-class objects. Programming language theorists
define a "first-class object" as a program entity that can be:

- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a function
- Returned as the result of a function


## What is a class
A class defines the nature of an object. It defines the data that can be stored
in an object and, the functions the object can perform.

A class defines a new namespace that can be used as the local scope of a type of object. You can
think of a class to be like an abstraction that defines the internal
representation of variables and functions associated with a type of object. In
simple terms, a class defines a type of object.

When we define a class, we are basically creating a new type of object. And since Python
is built with a "first-class everything" principle, there are several built-in
object types.

One of these built-in object types is the list object which is defined inside Python
with a `list` class. The `list`class defines a plethora of attributes, to build
a list object, to access and change elements in a list object, or to remove
elements from a list object, etc.

For example, we can build an empty list object by creating an instance
(assigning a class call to a variable) of the `list`class like this:

```
>>> x = list()

```

In the above example, we can say `x` is an instance of a `list` class
or `x` is a `list` object and with both statement we will mean the
same thing (although I think the second statement is cooler, *winks*)

We can manipulate `list` instance `x` by calling attributes that are defined inside
the `list` class on `x` using the dot notation. Let call the `list` class `append`
attribute on `x` to add an element to its list object like this:

```
>>> x.append(42)
>>> x.append(23)
>>> x
[42, 23]

```

The main built-in object types in Python are:

- integers (class name `int`)
- strings (class name `str`)
- lists (class name `list`)
- tuples (class name `tuple`)
- dictionaries (class name `dict`)

We can define custom classes for our Python programs by using the 
`class` keyword followed by an indented block of statements which form the
body of the class.

Lets create a simple robot class:

```
>>> class Robot(object):
...     """A simple Robot class"""
...     pass

```
In the above class definition, the body of the class consist of a single 
statement- `pass` -which indicates that we have an empty block. The words on 
the same line with the `class` keyword all make up the class header;  `Robot` is the 
name/type and  `object` (this is the default value for defining a basic class and it
can be omitted in a basic class definition) in the parentheses is the class parent. So we can say:

- `Robot` is a subclass/child of a Python `object` class, and inherits all its attributes.
- `object` is a superclass(can also be called parent class or base class) of `Robot`.

We can also make subclasses from our own custom classes too through a technique
based on the [inheritance]() principle of OOP.

## What is an object and an instance
An object is a region of allocated storage that is used to represent a value.

An object is a data structure that can contain functions as well as constants,
variables, and other data structure.

An instance is an individual occurence of an object.

When you call a class, the class call creates an object. When you assign the
created object to a variable, the variable becomes an instance of the class
that created the object assigned to it.

A class call is synonymous to what we've known as a function call.

In Python, object is also the name of the most basic class upon which other
classes are built. I know this might sound confusing but take a moment and
think of it this way, assume you're trying to build a house, first you need to
construct a solid foundation that can hold the weight of the house you want to
build. This foundation in Python terms is a class named `object` which is a
built-in type that defines the basic and necessary data and functions that is
needed support any other kind of class that a Python programmer might want to
create to suit their specific needs.


Let us create an instance of our `Robot` class which we defined earlier:
```
>>> p = Robot()

```
So `p` is now the name of a `Robot` class object or we say it is an instance of the `Robot` class:

```
>>> isinstance(p, Robot)
True
```

## What is the difference between a class and an object or instance
- A class defines the constants, variables, and functions that form the data 
structure of a particular object.
- An object is any data structure created by a class definition.
- An instance is an individual occurence of an object.

## What is an attribute

Functions and variables that defined inside a class are known as **methods** and
**fields** respectively. These **fields** and **methods** are collectively 
referred to as **attributes** of the class. 

**attributes** are of two types:

- Class attributes
- Instance attributes


**Class attributes**: these are attributes that are owned by a class and is 
shared by all the objects of the same class. We can access a class attributes 
via any of its instances (`instanceName.ClassAttribute`) or via the class name
(`ClassName.ClassAttribute`). There is only one copy of a class
attribute so when any change is made to a class variable, this change is seen 
in all it objects. We define class attributes outside all the methods. Usually 
they are placed at the top, right below the class header. 

**Instance attributes**: these are attributes that are owned by the respective
instances of a class. In this case, each instance has its own copy of the attribute
i.e they are not shared and are not related in any way to an attribute with the
same name in a different instance of the same class. We define instance attributes
inside methods. We can access an instance attribute only via its instance name.
(`instanceName.InstanceAttribute`)

According to how they can be accessed, all attributes in a class can be
separated into 3 groups: 

- public attributes
- private attributes 
- protected attributes

The Pythonic way to introduce attributes is to make them public. So by default
all attributes in a class are public attributes but they can be made to be
private attributes or protected attributes.

# What are and how to use public, protected and private attributes

According to their accessibilty, attributes can be
classified into:

- Private attributes: Are attributes that should only be used inside of the
class definition itself.
- Protected(restricted) attributes: Are attributes that should only be used under certain
conditions
- Public attributes: Are attributes that can and should be freely used inside
or outside of the class definition.


Python uses a special naming conventions for attributes in order to control their 
accessibility. Although not all of the naming conventions are enforced by
Python.

The convention(semi-enforced in Python) for naming a private attribute is to use
*double underscore* to prefix the attribute name i.e. `__privateAttribute`
and Python will use name-mangling to effectively make it a private attribute.

The convention(not enforced in Python but strongly recommended) for naming a 
protected attribute is to use *underscore* to prefix the variable name i.e. 
`_protectedAttribute`.

To summarize the attribute access type naming convention:

Naming style | access type | Meaning
--- | --- | ---
`varname` | Public | Attribute can be freely used inside or outside a class definition.
`_varname`| Restricted | Atrribute should not be used outside the class definition unless inside a subclass definition.
`__varname`| Private |  Attribute is inaccessible and invisible. it's neither possible to read nor write to this attribute, except inside the class

I'm taking a break from our `Robot` class to demostrate the behaviour of these
attributes types with an example class:
```
>>> class Test:
...     def __init__(self):
...             self.pub = "I am public"
...             self._proct = "I am protected"
...             self.__priv = "I am private"
>>> c = Test()
>>> c.pub
'I am public'
>>> c._proct
'I am protected'
>>> c.__priv
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  AttributeError: 'Test' object has no attribute '__priv'

```
from the above demostration, we can see that `__priv` is a private variable and
a call to it raises an `AttributeError` with a message saying "'Test' object
has no attribute '__priv'" when infact we do. This is how Python enforces the
privavcy of private variables

Now lets talk about some other things that where introduced in this
demostration..

## What is `self`

`self` is the parameter name used as a reference to an instance of a class.
As a matter of fact, `self` is not a Python keyword. It is just a
*strongly recommended* naming convention that you should use, as the name for
the first parameter in your method definitions.


There are many advantages to using this recommended naming convention - any
reader of your program will immediately recongnize it and even specialized IDEs
(Integrated Development Environments) can help you if use `self`.

## What is a method

Methods in Python are essentially functions that are defined inside a class
with a **compulsory first parameter** named `self` by convention. The presence
of `self` as the first parameter in the parameter list of a method definition
is the only specific difference between a method and an ordinary function. This
also means that even if you want to create a method that does not take any
arguments, you still have to include the `self` parameter in its definition.


We do not give a value for the `self` parameter when we call a method, Python
automatically provides its value.


Consider this example to understand how Python provides the value for the 
`self` parameter:

> Lets assume we have a class called `MyClass` and an object of this class
> called `myobject`. When we call a method of `MyClass` on `myobject` as 
> `myobject.method(arg1, arg2)`, this is implicitly converted by Python into
> `MyClass.method(myobject, arg1, arg2)`- this all the special `self` is about.

Coming back to our `Robot` class, lets define a simple method in it: 
```
>>> class Robot(object):
...     """A simple robot class"""
...
...     def say_hi(self):
...             """function that say a greeting"""
...             print("Hello, how are you")

```
We can now create a `Robot` class instance and call the `say_hi` method on the
instance:

```
>>> f = Robot()
>>> f.say_hi()
Hello, how are you

```

## What is the special `__init__` method and how to use it
The `__init__` method is used to initialize an instance and useful for defining
the attributes of an object. It is also part of a group of methods known as
**magic methods**.


The `__init__` name has special significance in a Python so it is not possible
to choose another name when defining this method. When Python sees the
`__init__` name during an instantiation (creation of an instance), it
automatically uses the values passed inside the class call to initialize object
attributes for the object been created.

If the `__init__` method is not defined in a class, Python will not be able to
uniquely distinguish between the objects created by different instances of the same class.


The `__init__` method can defined be anywhere inside the class definition, but
it is usually the first method to be defined in a class i.e it follows right
after the class header.

Lets define the `__init__` method for our `Robot` class.

```python

# robot.py

class Robot(object):
	"""A simple robot class"""

	def __init__(self, robo_name=None):
		"""initialization method"""
		self.name = robo_name
		print("__init__ has been executed!")


	def say_hi(self):
		"""A simple method"""
		if self.name:
			print("Hello, my name is {}".format(self.name))
		else:
			print("Hi, I am a robot without a name")
```
In the above example, I define the `__init__` method to take a parameter
`robo_name`(along with the usual `self`, you can use any number of paramters
with any name of your choice). Inside `__init__`, I created an object
attribute `name`. The `self` dot notation is used to create object attributes.
`self.name` means that `name` is an attribute of the object `self` (Recall
`self` is parameter takes the instance name as its value). `robo_name` is a
local variable of the `__init__`
method (just like parameters are for regular functions). Now lets create
instances of our `Robot` to see how they behave with respect to the modification
I just described:

**NB:** since the lines of codes in our class definition has increased I saved the
code in a file named 'robot.py' so I can import it as a module into the
interactive Python shell:

```
>>> from robot import Robot
>>> p = Robot()
__init__ has been executed!
>>> x = Robot('Driod')
__init__ has been executed!
>>> p.say_hi()
Hi, I am a robot without a name
>>> x.say_hi()
Hello, my name is Driod

```

Before now, all the `Robot` class objects we created were not initialized because we
had not defined the `__init__` method. But with the `__init__` method now 
defined inside our `Robot` class, when creating the instances `p` and `x` of
the `Robot` class, the `print` statement inside the `__init__` method is
executed immediately afterward and also if an argument is passed into the
parentheses of the class call during instatiation, the object that is created is
initialized with that value as is the case with instance `x`.

We do not explicitly call the `__init__` method on an object because Python
automatically calls it immediately after an object is created. This
is the special significance of this method.


## What is Data Abstraction, Data Encapsulation, and information Hiding
Data abstraction is the principle of using data encapsulation and data
hiding together in a class definition.
```
 Data Abstraction = Data Encapsulation + Data Hiding
```
Data encapsulation is the principle of hiding unnecessary details of a class
definition. it is seen as the bundling of data with the methods that
operate on that data, this is often accomplished by providing two kinds of methods
for attributes: getter methods and setter methods.


Getter methods(or accessors) are used to return the values of attributes without
changing the values while setter methods(or mutators) are used to change the
values of attributes without returning the values.


lets define a getter and setter for the object attribute `name` in our
`Robot` class:

```python
# robot.py

class Robot(object):
	"""A simple robot class"""
	def __init__(self, robo_name=None):
		"""initialization method"""
		self.name = robo_name
		print("__init__ has been executed!")


	def say_hi(self):
		"""A simple method"""
		if self.name:
			print("Hello, my name is {}".format(self.name))
		else:
			print("Hi, I am a robot without a name.")

	def set_name(self, robo_name):
		"""setter method for the robo_name attribute"""
		self.name = robo_name

	def get_name(self):
		"""getter method for the robo_name attribute"""
		return self.name

```
OUTPUT

```bash
>>> p = Robot('Driod1')
__init__ has been executed!
>>> print(p.get_name())
Driod1
>>> x = Robot()
__init__ has been executed!
>>> x.say_hi()
Hi, I am a robot without a name.
>>> x.set_name('Driod2')
>>> x.say_hi()
Hello, my name is Driod2
```

Data encapsulation via methods doesn't neccessarily mean that the data is
hidden. You might be capable of accessing and seeing that data anyway, like for
example we can still access the `name` attribute without using the getter and
change its value without using the setter:

```bash
>>> p = Robot('Driod1')
__init__ has been executed!
>>> print(p.name)
Driod1
>>> p.name = "Bot1"
>>> print(p.name)
Bot1
```

But using these-getter and setter-methods is recommended because with them, you
will be able to validate the assignment of a private attribute and also define
how getting the attribute value will be available from outside-by copy? by
assignment? etc. Also, adding type/value validation in the setter will
centralize the logic, since we will do it in only one place. 

So, to ensure that users of our class can only use the getter and setter 
methods we've specified for certain attributes in our class, we have
to hide the data.

Data hiding is the principle that some internal information or data is
"hidden"(think private attributes), so that it can't be directly accessed and 
its value can't be accidentally changed. 

Proper data encapsulation means, that we should only be able to access private
attributes via getters and setters. Hence data abstraction.

Now we have to rewrite our `Robot` class so that the getter and setter methods
for the `name` attribute are the only way to access it. To achieve this we 
have to replace each occurence of `self.name` with `self.__name`:

```python

class Robot(object):
	"""A simple robot class"""

	def __init__(self, robo_name=None):
	"""initialization method"""
		self.__name = robo_name
		print("__init__ has been executed!")


	def say_hi(self):
		"""A simple method"""
		if self.__name:
			print("Hello, my name is {}".format(self.__name))
		else:
			print("Hi, I am a robot without a name")
	
	def set_name(self, robo_name):
		"""setter method for the robo_name attribute"""
		self.__name = robo_name
	
	def get_name(self):
		"""getter method for the robo_name attribute"""
		return self.__name

```
Now if we try to access `name` directly, we will get an error:

```bash
p = Robot()
p.name = 'Driod1'

```

## What is a property
The getter and setter method are collectively called accessors. A property is 
an attribute that is defined through its accessors.



## What is the difference between an attribute and a property in Python

## What is the Pythonic way to write getters and setters in Python
The Pythonic way to introduce attributes is to make them public.

## How to dynamically create arbitrary new attributes for existing instances of a class 

## How to bind attributes to objects and classes


## What is the `__dict__` of a class and/or instance of a class and what does it contain

Remember earlier we learnt that a class created with an `object` parent class
inherits all the attributes of a Python object? Yes. So one of those inherited 
attributes is the `__dict__` attribute which is an empty dictionary.

Class attributes and object attributes are stored in separate instances of the 
`__dict__` attribute inside a class. You don't actually see how this
`__dict__` attribute is implemented due to the OOP technique known as 
**encapsulation** but, just know that you have it.

So continuing with our example `Robot` class, let us check the respective 
attributes of our class and its object:

```python

# Create a simple class
class Robot(object):
	"""A simple robot class.

	Attributes:
		a (str): Human readable string
		b (int): Number

	"""

	a = "I am a class attribute" 
	b = 34

	def say_hi(self):
	"""A simple method"""
		print('Hello, how are you')


# Create an instance of the Robot class
p = Robot()

# print the class attributes of Robot class
print(Robot.__dict__)

print('-----')

# print the attributes of Robot class object
print(p.__dict__)

```
OUTPUT

```
{'__module__': '__main__', '__doc__': 'A simple robot class.\n\n
Attributes:\n        a (str): Human readable string\n        b (int):
Number\n\n    ', 'a': 'I am a class variable', 'b': 34, 'say_hi': <function
Robot.say_hi at 0x7fb127dd9c10>, '__dict__': <attribute '__dict__' of 'Robot'
objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>}
----------
{}

```
In the output we see that the class attribute dictionary contains as keys, the names of
the method and field that we defined in our class. It also has some keys from 
values we didn't define. Yes. These values are also part of the
inherited attributes of the Python object we talked about earlier.

But as we can see, our object attribute dictionary is empty. This is because 
we have not defined any instance variable for our `Robot` class.

## How does Python find the attributes of an object or class

If you try to access an attribute in a class, Python checks first, if the
attribute name is a key in the object attribute dictionary. if it is not, 
Python then checks, if the attribute name is a key in the class attribute
dictionary. And if it is, the value will be retrieved.

> An instance attribute will take precedence over a class attribute if it 
> has the same name as the class attribute.

If an attribute name is not included in either of the dictionaries, the attribute
name is not defined. An `AttributeError` is raised, if you try to access an 
undefined attribute. lets access the attributes in our `Robot` class:

```python

# Create a simple class
class Robot(object):
	"""A simple robot class.

	Attributes:
		a (str): Human readable string
		b (int): Number

	"""

	a = "I am a class attribute" 
	b = 34

	def say_hi(self):
	"""A simple method"""
		print('Hello, how are you')


# Create an instance of the Robot class
p = Robot()

# Try the following codes below on your terminal see what happens

# print the class attributes values of `Robot` class
print(Robot.a)
print(Robot.b)
print(Robot.c) # This will raise an AttributeError
Robot().say_hi()
Robot.say_hi(p)
print('-----')

# print the class attributes values through `Robot` class object p
print(p.a)
print(p.b)
print(p.c) # This will raise an AttributeError 

print('-----')

# create another instance of the `Robot`class
x = Robot()

print('-----')

# print the class attributes through Robot class object `x`
print(x.a)
print(x.b)

print('-----')

# change the value of `Robot` class attribute `a` through Robot class object `x`
x.a = 23 # Changing class attributes  this way is Not recommend 

# Change the value of `Robot` attribute `b` 
Robot.b = "I was changed from a number" # The recommended way

print('-----')

# print the values of `Robot` class attributes through `Robot` class object `p`
print(p.a)
print(p.b)

```

## How to use the getattr function





## Resources
- [Object Oriented Programming {video}](https://www.youtube.com/watch?v=-DP1i2ZU9gk)
- [Obeject Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [object](https://stackoverflow.com/a/56310340) 
