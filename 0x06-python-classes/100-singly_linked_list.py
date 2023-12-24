#!/usr/bin/python3
"""
Module that defines a Node and SinglyLinkedList class
"""


class Node:
    """
    Node class for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance

        Args:
            data: The data of the node.
            next_node: The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data attribute

        Args:
            value: The data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node attribute

        Args:
            value: The next node to set.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty head
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value: The value to insert.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        String representation of the linked list
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
