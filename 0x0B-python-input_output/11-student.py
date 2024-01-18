#!/usr/bin/python3
"""
Defines a class that is based on the previous task (10-student.py).
"""


class Student:
    """
    Represents a student with attributes: first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: A dictionary containing attributes and their values.
        """
        if attrs is None or not attrs:
            return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        return {attr: getattr(self, attr, None) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance with the provided dictionary.

        Args:
            json (dict): A dictionary with attribute names as keys and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
