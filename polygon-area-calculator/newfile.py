class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
    
    def set_width(self, amount):
        if amount <= 0:
            raise ValueError("Width must be positive.")
        self.width = amount
    
    def set_height(self, amount):
        if amount <= 0:
            raise ValueError("Height must be positive.")
        self.height = amount
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return (width ** 2 + height ** 2) ** 0.5

    def get_picture(self):
        if (self.width > 50) or (self.height > 50):
            return ("Too big picture.")
        else:
            myPic = ""
            for x in range(self.height):
                for y in range(self.width):
                    myPic += "*"
                myPic += '/n'
            return myPic

    def get_amount_inside(self, shape):
        a = int(self.height / shape.height)
        b = int(self.width / shape.width)
        return a*b
    

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
    
    def __str__(self):
        return "Square(side="+ str(self.side) + ")"
    
    def set_side(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

my_rec = Rectangle(34,65)
mysquare = Square(5)
print(my_rec.get_amount_inside(mysquare))
print(my_rec)