# Object Oriented Programming

### 1. Why Python programming is awesome:

Python is considered awesome for several reasons:
- **Readability**: Python has a clear and readable syntax, making it easy for beginners to learn and write code.
- **Extensive Libraries**: Python has a rich set of libraries and frameworks for various tasks, reducing the need to write code from scratch.
- **Community Support**: It has a large and active community, providing support, tutorials, and a wealth of resources.
- **Versatility**: Python is versatile and can be used for web development, data analysis, artificial intelligence, machine learning, automation, and more.
- **Ease of Learning**: Its simplicity and readability make it accessible for beginners while remaining powerful for advanced users.
- **Open Source**: Python is open-source, allowing users to contribute and modify the language.

### 2. What is an object:

In Python, an object is a fundamental element of the language. Everything in Python is an object, which means it has a type and can be manipulated using methods associated with that type.

### 3. What is the difference between a class and an object or instance:

- **Class**: A class is a blueprint or template for creating objects. It defines attributes and methods common to all instances of that class.
- **Object or Instance**: An object is an instantiation of a class. It is a concrete entity created from the class, possessing the defined attributes and behaviors.

### 4. What is the difference between immutable object and mutable object:

- **Immutable Object**: An object whose state cannot be modified after it is created. Examples in Python include strings, tuples, and frozensets.
- **Mutable Object**: An object that can be modified after it is created. Examples in Python include lists, dictionaries, and sets.

### 5. What is a reference:

A reference in Python is a value that refers to the memory location of an object. Variables in Python are references to objects.

### 6. What is an assignment:

Assignment is the process of binding a value to a variable. It associates a name (the variable) with a value, allowing you to refer to and manipulate that value using the variable.

### 7. What is an alias:

An alias is an alternative name or reference to the same object. When two variables refer to the same object, they are considered aliases.

### 8. How to know if two variables are identical:

Use the `is` keyword to check if two variables reference the same object. For example:
```python
a = [1, 2, 3]
b = a
print(a is b)  # True
```

### 9. How to know if two variables are linked to the same object:

Use the `id()` function to get the identity (memory address) of an object and compare them. For example:
```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True
```

### 10. How to display the variable identifier:

Use the `id()` function to get the memory address of an object. For example:
```python
a = [1, 2, 3]
print(id(a))  # Memory address of the list 'a'
```

### 11. What is mutable and immutable:

- **Mutable**: Objects whose state or value can be changed after creation.
- **Immutable**: Objects whose state or value cannot be changed after creation.

### 12. What are the built-in mutable types:

Examples of built-in mutable types in Python include lists, dictionaries, and sets.

### 13. What are the built-in immutable types:

Examples of built-in immutable types in Python include integers, floats, strings, tuples, and frozensets.

### 14. How does Python pass variables to functions:

Python uses a mechanism called "call by object reference" or "call by sharing." When a variable is passed to a function, a reference to the object is passed. If the object is mutable and is modified within the function, the changes are visible outside the function. If the object is immutable, the function receives a copy, and changes within the function do not affect the original object.
