#!/usr/bin/python3
import base 
import rectangle
from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object with the given size, position, and optional id."""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Return a string representation of the Square object."""
        class_name = self.__class__.__name__
        return f"[{class_name}]  ({self.id}) {self.x}/{self.y} - {self.size}"
        
    @property
    def size(self):
        """Return the size of the Square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the Square, raising errors for invalid values."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0: 
            raise ValueError("size must be greater than zero")
        else:
            self.__size = value
   
    def update(self, *args, **kwargs):
        """Update attributes based on either positional or keyword arguments."""
        if len(args) > 0:
            # If positional arguments exist, update attributes in the order they are defined
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
            return str()
        else:
             # If no positional arguments, update attributes using keyword arguments 
            for key, value in kwargs.items():
                setattr(self, key, value)
            return str()

    def to_dictionary(self):
        """Return a dictionary representation of the Square object."""
        myDictionary = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return myDictionary

