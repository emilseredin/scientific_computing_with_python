class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
       return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        for line in range(self.height):
            picture += "".join(["*" for col in range(self.width)])
            picture += "\n"
        return picture

    def get_amount_inside(self, rectangle):
        return (self.height // rectangle.height) * (self.width // rectangle.width)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.height = self.width = side

    def set_side(self, side):
        self.height = self.width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __repr__(self):
        return f"Square(side={self.width})"
