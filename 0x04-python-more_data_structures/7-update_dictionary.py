#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to replace or add.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

# Test the function with the provided example
a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")

# Print the updated dictionary
for key, value in new_dict.items():
    print("{}: {}".format(key, value))

print("--")

# Print the original dictionary
for key, value in a_dictionary.items():
    print("{}: {}".format(key, value))

print("--")
print("--")

# Test with a new key
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")

# Print the updated dictionary
for key, value in new_dict.items():
    print("{}: {}".format(key, value))

print("--")

# Print the original dictionary
for key, value in a_dictionary.items():
    print("{}: {}".format(key, value))
