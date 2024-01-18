#!/usr/bin/python3
"""
Defines a student class based on previous task (9-student.py).
"""


class Student:
    """
    Defines a student by:
    - Public instance attributes: first_name, last_name, age
    - Instantiation with first_name, last_name, and age
    - Public method to_json retrieves dictionary of Student instance
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

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
            attrs (list): List of strings - attribute names to be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        # If attrs is not specified, retrieve all attributes
        if attrs is None or not attrs:
            return {}
        return {attr: getattr(self, attr, None) for attr in attrs if hasattr(self, attr)}
