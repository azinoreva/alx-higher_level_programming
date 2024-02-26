#!/usr/bin/python3
""" Importing important modules and libraries """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None): 
        """ initialized a new rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height= height
        self.__x = x
        self.__y = y
        
        super().__init__(id)

    @property
    def width(self):
        """ making width accessible """
        return self.__width
    
    @width.setter
    def width (self, value):
        """ defining and setting the width """
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value <= 0: 
            raise ValueError("width must be greater than zero")
        else:
            self.__width = value

    @property
    def height(self):
        """ making height accessible """
        return self.__height
    
    @height.setter
    def height (self, value):
        """ defining and setting the height """
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        if value <= 0: 
            raise ValueError("height must be greater than zero")
        else:
            self.__height = value
    
    @property
    def x(self):
        """ making x accessible """
        return self.__x
    
    @x.setter
    def x (self, value):
        """ defining and setting x """
        if not isinstance(value,int):
            raise TypeError("x must be an integer")
        if value <= 0: 
            raise ValueError("x must be greater than zero")
        else:
            self.__x = value

    @property
    def y(self):
        """ making y accessible """
        return self.__y
    
    @y.setter
    def y (self, value):
        """ defining and setting y """
        if not isinstance(value,int):
            raise TypeError("y must be an integer")
        if value <= 0: 
            raise ValueError("y must be greater than zero")
        else:
            self.__y = value

    def area(self):
        """ Calculate and return the area of the rectangle """
        return (self.width * self.height)
   
    def display(self):
        """ Display the rectangle using '#' characters """
        for i in range(self.height):
            print('#' * self.width)
            i += 1 

    def __str__(self):
       """ Return a string representation of the rectangle object """
       class_name = self.__class__.__name__
       return f"[{class_name}]  ({self.id}) {self.__x}/{self.__y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """ Update attributes based on either positional or keyword arguments """
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

