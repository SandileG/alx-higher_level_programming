#  Import Modules

# 1. Why Python programming is awesome:
Python is an awesome programming language for several reasons. It emphasizes readability and simplicity, making it easy to learn and use. It has a vast and active community, extensive libraries, and frameworks, enabling developers to accomplish tasks efficiently. Python is versatile, suitable for various applications, including web development, data science, artificial intelligence, automation, and more. Its syntax promotes clean and concise code, fostering a productive development experience.

# 2. How to import functions from another file:
To import functions from another file in Python, you can use the import statement. Let's assume you have a file named my_module.py with a function called my_function. To import it into another Python script, use:

from my_module import my_function

# 3. How to use imported functions:
Once a function is imported, you can use it in your script just like any other function. For example:

result = my_function(argument1, argument2)

# 4. How to create a module:
A module in Python is simply a Python script. To create a module, save your Python code in a file with a .py extension. This file can then be imported into other scripts as a module.

# 5. How to use the built-in function dir():
The dir() function in Python is used to list the names in the current local scope or the attributes of an object. For example:

my_list = [1, 2, 3]
print(dir(my_list))
This will show all the methods and attributes available for the list object.

# 6. How to prevent code in your script from being executed when imported:
To prevent code from being executed when a script is imported, you can use the if __name__ == "__main__": construct. Place the code you want to execute only when the script is run directly under this condition. For example:

def my_function():
    # Function code

if __name__ == "__main__":
    # Code to be executed when the script is run directly
    my_function()

# 7. How to use command line arguments with your Python programs:
You can use the sys or argparse module to handle command line arguments. For example, using argparse:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to the input file")
args = parser.parse_args()

print("Input file:", args.input_file)
This script expects an input file as a command line argument and prints its path.
