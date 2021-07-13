import turtle

t = turtle.Turtle() # first turtle pen 

# changing the turtle pen shape (turtle, arrow, circle, etc.)
t.shape("turtle")

# changing the turtle and pen color
# color database for turtle: https://trinket.io/docs/colors
t.color("black", "gold")  # first is for pen, second is for turtle
colorstrings = ["red","orange","yellow","green","blue","indigo","violet"]
cInd = 0
# changing the pen speed (0-10, slowest to fastest)
t.speed(3)

lineT = turtle.Turtle()
lineT.hideturtle()
lineT.lt(90)
lineT.speed(10)

ITERATIONS = 12
#Set starting spiral size and number of iterations
n2 = 0
n1 = 1
for i in range(ITERATIONS):
  c = n2 + n1
  #fibbonacci
  t.pencolor(colorstrings[cInd])
  cInd = (cInd + 1) % 7
  #change the color for fun
  t.circle(c,90)
  #draw the next section of the spiral

  x,y = t.pos()
  lineT.penup()
  lineT.setpos(x,y)
  #bring the fast turtle over to draw a box
  lineT.lt(90)
  lineT.pendown()
  for s in range(4):
    lineT.fd(c)
    lineT.lt(90)

  n2 = n1
  n1 = c
  
turtle.done()
