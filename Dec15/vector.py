class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, value):
        if isinstance(value, Vector2):
            return Vector2(self.x + value.x, self.y + value.y)
        else:
            return Vector2(self.x + value, self.y + value)
    
    def __sub__(self, value):
        return self.__add__(value*-1)

    def __mul__(self, value):
        return Vector2(self.x * value, self.y * value)

    def __floordiv__(self, value):
        return Vector2(self.x // value, self.y // value)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))