import random

class Square:    
    def __init__(self, x, y, size, level=0):
        self.x = x
        self.y = y
        self.size = size
        self.level = level

    def split(self):
        half = self.size / 2
        level = self.level + 1
        return [
            Square(self.x, self.y, half, level),
            Square(self.x + half, self.y, half, level),
            Square(self.x, self.y + half, half, level),
            Square(self.x + half, self.y + half, half, level)
        ]
    
    def get_rect(self):
        return (int(self.x), int(self.y), int(self.size))
    
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)