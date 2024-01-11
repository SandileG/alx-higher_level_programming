# Inheritance

# General:**
Python is a versatile, high-level programming language that emphasizes readability and ease of use. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's syntax is clear and concise, making it an excellent choice for beginners and experienced developers alike. It has a vast standard library and a large community, contributing to its widespread adoption in various domains such as web development, data science, artificial intelligence, and more.

# Why Python programming is awesome:
   - **Readability:** Python code is easy to read and write, contributing to better code maintainability.
   - **Versatility:** Python can be used for various applications, including web development, data analysis, machine learning, and more.
   - **Extensive Libraries:** Python has a rich ecosystem of libraries and frameworks that simplify complex tasks.
   - **Community Support:** A large and active community provides resources, documentation, and support.

# What is a superclass, base class, or parent class:
   - A superclass, base class, or parent class in object-oriented programming is a class from which other classes (subclasses or derived classes) can inherit attributes and methods.

# What is a subclass:
   - A subclass is a class that inherits attributes and methods from a superclass or base class. It can also have its own additional attributes and methods.

# How to list all attributes and methods of a class or instance:
   - You can use the `dir()` function to list all attributes and methods of a class or an instance of that class.

# When can an instance have new attributes:
   - An instance can have new attributes at any time. You can assign new attributes to an instance like this: `instance.new_attribute = value`.

# How to inherit class from another:
   - Inheritance in Python is accomplished by specifying the base class in parentheses after the derived class name. Example: `class DerivedClass(BaseClass):`.

# How to define a class with multiple base classes:
   - You can define a class with multiple base classes by separating them with commas. Example: `class DerivedClass(BaseClass1, BaseClass2):`.

# What is the default class every class inherits from:
   - The default class every class inherits from in Python is `object`. If you don't explicitly specify a base class, your class implicitly inherits from `object`.

# How to override a method or attribute inherited from the base class:
    - To override a method or attribute, define a method or attribute with the same name in the subclass. This process is known as method or attribute overriding.

# Which attributes or methods are available by heritage to subclasses:
    - Subclasses inherit all attributes and methods from the superclass unless overridden. They can access these inherited members using dot notation.

# What is the purpose of inheritance:
    - Inheritance facilitates code reuse and promotes the creation of a hierarchical structure. It allows new classes to be built upon existing ones, inheriting their functionality while providing room for customization.

# What are, when and how to use isinstance, issubclass, type, and super built-in functions:
    - **isinstance(obj, class):** Checks if the object is an instance of the specified class.
    - **issubclass(subclass, class):** Checks if a class is a subclass of another class.
    - **type(obj):** Returns the type of the object.
    - **super():** Returns a temporary object of the superclass, allowing you to call its methods.

   These functions are used for type checking, inheritance checks, and accessing the superclass in object-oriented programming. They are helpful in creating flexible and robust code.
