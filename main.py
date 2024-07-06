#Turtle Party Project
#by Adam Stevenson
# 7.6.24


import turtle

turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def moveFor(len): #forward helper function by going back 
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.right(360 / num)
  
def spiral (len, angel):
  for i in range(len, 5, -5):
    turtle.forward (i)
    turtle.right(angel)
    
spiral (75, 45) # circular
moveFor (150)
turtle.color('blue')
spiral (100, 90) #square
moveFor (200)
# polygon(3, 10)

for n in range(3, 10): #clock style polygon
  moveFor(50) #forward
  polygon(n, 100 / n)
  back(50)
  turtle.right(360 / 7)
