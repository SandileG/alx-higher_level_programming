#!/usr/bin/python3
"""
Defines class that has various attributes of student instance.
"""


class Student:
    """
    Defines a student by:
    - Publis instance attributes: first_name, last_name, age
    - Instantiation with first_name, last_name, and age
    - Public method to_json that retrieves dictionary of Student instance
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last_name of the student.
            age (int): THe age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Studen instance.
        """

        # Get the dictionary representation of the object's attributes
        obj_dict = self.__dict__.copy()

        # Convert non-serializable attributes to serializable formats
        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                continue
            elif hasattr(value, '__dict__'):
                obj_dict[key] = value.__dict__.copy()
            else:
                obj_dict[key] = str(value)

        return obj_dict
