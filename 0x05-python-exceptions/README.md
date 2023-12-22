# Python Exceptions

# Why Python programming is awesome:

Python is known for its simplicity and readability, making it an excellent language for beginners and experienced developers alike.
It has a vast standard library and a large ecosystem of third-party packages, contributing to its versatility and ease of development.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
The Python community is vibrant and supportive, with extensive documentation and a wealth of online resources.

# Difference between errors and exceptions:

Errors are unexpected problems that occur during the execution of a program and typically lead to the termination of the program.
Exceptions, on the other hand, are events that occur during the execution of a program but can be handled to prevent program termination.

# What are exceptions and how to use them:

Exceptions are events that disrupt the normal flow of a program. They are raised when an error occurs.
In Python, exceptions are objects that represent errors. They can be predefined (built-in) or user-defined.
To use exceptions, you enclose the code that might raise an exception in a try block and handle the exception in an associated except block.

# When do we need to use exceptions:

Exceptions are useful when dealing with unpredictable situations, such as reading from a file that may not exist, dividing by zero, or trying to access an index beyond the bounds of a list.
They provide a structured way to handle errors and prevent unexpected program termination.

# How to correctly handle an exception:

Place the code that might raise an exception in a try block.
If an exception occurs, the control is transferred to the corresponding except block.
The except block contains the code to handle the exception, allowing the program to continue running.

# Purpose of catching exceptions:

Catching exceptions allows a program to gracefully handle errors without crashing.
It enables the program to recover from exceptional conditions, log relevant information, and take appropriate actions.

# How to raise a built-in exception:

You can raise a built-in exception using the raise keyword followed by the exception type.
For example, raise ValueError("Invalid value") raises a ValueError with a custom error message.

# When to implement a clean-up action after an exception:

Clean-up actions, like closing files or network connections, are implemented in a finally block.
A finally block is executed whether an exception is raised or not, making it suitable for releasing resources and ensuring cleanup operations.
