# Input/ Output

# Why Python Programming is Awesome:
* Readability: Python emphasizes readability and simplicity, making it easy for beginners to learn and write code.
* Versatility: Python is a versatile language used in various domains, including web development, data science, artificial intelligence, automation, and more.
* Extensive Libraries: Python has a rich set of libraries and frameworks that accelerate development and provide solutions for various tasks.
* Community Support: A large and active community contributes to the language's growth, offering help, resources, and a vast collection of third-party packages.

# File Handling:
How to Open a File:

file = open('filename.txt', 'r')  # 'r' for reading, 'w' for writing, 'a' for appending

# How to Write Text in a File:

with open('filename.txt', 'w') as file:
    file.write('Hello, this is some text.')

# How to Read the Full Content of a File:

with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)

# How to Read a File Line by Line:

with open('filename.txt', 'r') as file:
    for line in file:
        print(line)

# How to Move the Cursor in a File:
The cursor automatically moves when reading line by line or using methods like read().

# How to Make Sure a File is Closed After Using It:
The with statement automatically closes the file when the block is exited.

# What is and How to Use the with Statement:
The with statement is used for resource management. It ensures that clean-up code is executed, like closing a file.

# JSON (JavaScript Object Notation):
* What is JSON:
JSON is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

# What is Serialization:
Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted, such as JSON.

# What is Deserialization:
Deserialization is the process of converting a serialized format (like JSON) back into a data structure or object.

# How to Convert a Python Data Structure to a JSON String:

import json
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)

# How to Convert a JSON String to a Python Data Structure:

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
