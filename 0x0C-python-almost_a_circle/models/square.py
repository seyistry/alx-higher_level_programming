#!/usr/bin/python3
"""A Rectangle model class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A simple Square module"""

    def __init__(self, size, x=0, y=0, id=None):
        """class Square constructor

        Args:
            size (_type_): _description_
            x (int): _description_. Defaults to 0.
            y (int): _description_. Defaults to 0.
            id (_type_): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
                self.height = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.width}
