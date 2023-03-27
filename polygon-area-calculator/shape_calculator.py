
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self,w):
    self.width = w
    
    

  def set_height(self,h):
    self.height = h

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2*self.width + 2*self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2)**0.5)

  def get_picture(self):
    if (self.width > 50 or self.height>50):
      return("Too big for picture.")
    else:
      mystr = ""
      for x in range(self.height):
        for i in range(self.width):
          mystr = mystr + "*"
        mystr = mystr + "\n"
      print(mystr)
      return (mystr)
      
  def get_amount_inside(self, shape):
    a = int(self.height / shape.height)
    b = int(self.width / shape.width)
    return (a*b)

class Square(Rectangle):
  def __init__(self, side):
    self.side = side
    Rectangle.__init__(self, side, side)
  
  def set_side(self,side):
    self.side = side
    super().__init__( side, side)

  def set_width(self,w):
    self.side = w
  def set_height(self,h):
    self.height = h
    
  def __str__(self):
    return "Square(side=" + str(self.side) + ")"
  