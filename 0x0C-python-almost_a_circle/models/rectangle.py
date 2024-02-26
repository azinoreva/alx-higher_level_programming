#!/usr/bin/python3
""" Importing important modules and libraries """
import base
from base import Base

""" Rectangle class """
class Rectangle(Base):

    """ initialized the function that represents """
    def __init__(self, width, height, x=0, y=0, id=None): 
        self.__width = width
        self.__height= height
        self.__x = x
        self.__y = y
        """ taking id from base """
        super().__init__(id)

    """ making width accessible """
    @property
    def width(self):
        return self.__width
    
    """ defining and setting the width """
    @width.setter
    def width (self, value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value <= 0: 
            raise ValueError("width must be greater than zero")
        else:
            self.__width = value

    """ making height accessible """   
    @property
    def height(self):
        return self.__height
    
    """ defining and setting the height """
    @height.setter
    def height (self, value):
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        if value <= 0: 
            raise ValueError("height must be greater than zero")
        else:
            self.__height = value
    
    """ making x accessible """ 
    @property
    def x(self):
        return self.__x
    
    """ defining and setting x """
    @x.setter
    def x (self, value):
        if not isinstance(value,int):
            raise TypeError("x must be an integer")
        if value <= 0: 
            raise ValueError("x must be greater than zero")
        else:
            self.__x = value

    """ making y accessible """
    @property
    def y(self):
        return self.__y
    
    """ defining and setting y """
    @y.setter
    def y (self, value):
        if not isinstance(value,int):
            raise TypeError("y must be an integer")
        if value <= 0: 
            raise ValueError("y must be greater than zero")
        else:
            self.__y = value

    """ Calculate and return the area of the rectangle """ 
    def area(self):
        return (self.width * self.height)
   
    """ Display the rectangle using '#' characters """ 
    def display(self):
        for i in range(self.height):
            print('#' * self.width)
            i += 1 

    """ Return a string representation of the rectangle object """ 
    def __str__(self):
       class_name = self.__class__.__name__
       return f"[{class_name}]  ({self.id}) {self.__x}/{self.__y} - {self.width}/{self.height}"
    
    """ Update attributes based on either positional or keyword arguments """
    def update(self, *args, **kwargs):
        if len(args) > 0:
            # If positional arguments exist, update attributes in the order they are defined
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
            return str()
        else:
            # If no positional arguments, update attributes using keyword arguments 
            for key, value in kwargs.items():
                setattr(self, key, value)
            return str()
        
    """ Return a dictionary representation of the rectangle object """ 
    def to_dictionary(self):
        myDictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return myDictionary

