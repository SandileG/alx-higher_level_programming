# Classes & Objects

# Why Python programming is awesome:

Python is known for its simplicity and readability, making it easy to learn and use.
It has a large standard library and a vibrant ecosystem of third-party packages.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

#What is OOP (Object-Oriented Programming):

OOP is a programming paradigm that uses objects, which are instances of classes, for structuring and organizing code.
It involves concepts such as encapsulation, inheritance, and polymorphism to model real-world entities and their interactions.

# “First-class everything”:

In Python, everything is considered an object, and objects can be assigned to variables, passed as arguments, and returned from functions—treating them as "first-class citizens."

# What is a class:

A class is a blueprint for creating objects. It defines attributes and methods that the objects instantiated from the class will have.

# What is an object and an instance:

An object is an instance of a class. It is a concrete entity created from a class, with specific values for its attributes.
The terms "object" and "instance" are often used interchangeably.

# Difference between a class and an object or instance:

A class is a blueprint or template for creating objects, while an object (or instance) is a concrete instantiation of that class.

# What is an attribute:

An attribute is a value associated with an object. In Python classes, attributes are variables that store data.

# Public, protected, and private attributes:

Public attributes are accessible from outside the class.
Protected attributes have a single leading underscore and are considered internal, but they can still be accessed.
Private attributes have a double leading underscore and are name-mangled to make them more challenging to access directly from outside the class.

# What is self:

self is a conventionally used name for the first parameter of methods in a class. It refers to the instance of the class and is used to access its attributes and methods.

# What is a method:

A method is a function defined within a class. It operates on the attributes of an instance of the class.

# Special init method and how to use it:

__init__ is a special method in Python classes used for initializing object attributes when an object is created.

# Data Abstraction, Data Encapsulation, and Information Hiding:

Data Abstraction: Presenting only the essential features of an object and hiding the implementation details.
Data Encapsulation: Bundling the data (attributes) and the methods that operate on the data into a single unit (class).
Information Hiding: Restricting access to certain details of an object and revealing only what is necessary.

# What is a property:

A property is a special kind of attribute that is accessed like an attribute but may involve custom getter and setter methods.

# Difference between an attribute and a property in Python:

An attribute is a simple value associated with an object.
A property is a special kind of attribute that may have custom getter and setter methods.

# Pythonic way to write getters and setters:

Use the @property decorator for getters and the @<property_name>.setter decorator for setters.

# How to dynamically create arbitrary new attributes:

You can dynamically create attributes using the setattr() function.

#How to bind attributes to object and classes:

Attributes are bound to objects by assignment (self.attribute = value), and they can also be bound to classes.

# What is the dict of a class and/or instance:

__dict__ is a dictionary containing the namespace of a class or instance. It holds the attributes and methods of the object.

# How does Python find the attributes of an object or class:

Python looks for attributes first in the instance's namespace, then in the class's namespace, and finally in the namespaces of the base classes (if any).

# How to use the getattr function:

getattr(object, 'attribute_name') is used to get the value of the attribute with the specified name from the object.
