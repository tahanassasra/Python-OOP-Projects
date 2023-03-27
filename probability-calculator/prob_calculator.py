import copy
import random
# Consider using the modules imported above.
class Hat:
    def __init__(self,**arg):
        self.mydict = dict(arg)
        self.contents = list()
        for key,value in self.mydict.items():
            for i in range(value):
                self.contents.append(key)
      
    def draw(self, x):
      self.drawn = []
      if (x > len(self.contents)):
        self.drawn = self.contents
        self.contents = []
      else:
        for i in range(x):
          ran = random.choice(self.contents)
          self.contents.remove(ran)
          self.drawn.append(ran)
      return self.drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0

  for i in range(num_experiments):
    y=0
    temphat = copy.deepcopy(hat)
    drawn_balls = hat.draw(num_balls_drawn)
    hat = copy.deepcopy(temphat)
    

    mydrawn_dict = dict()
    for color in drawn_balls:
      mydrawn_dict[color] = mydrawn_dict.get(color,0) + 1

    for color in mydrawn_dict:
      expected_balls[color] = expected_balls.get(color,0)
    for color in expected_balls:
      mydrawn_dict[color] = mydrawn_dict.get(color,0)
    
    
    for color in mydrawn_dict:
      if mydrawn_dict[color] >= expected_balls[color]:
        y = y+1
      else:
        break
    if y == len(mydrawn_dict): #all drawn balls have at leasted expected number
      m = m+1
  return (m/num_experiments)