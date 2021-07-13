import turtle
import random

NUM_LAND = 4
NUM_BRIDGE = 7
RANDOM = False

t = turtle.Turtle()
t.hideturtle()

t.speed(10)
t.penup()
t.setposition(-250,250)
t.pendown()
for x in range(4):
  t.fd(500)
  t.rt(90)

def get_orth(e1, e2, n):
  direct_vector = (e2[0]-e1[0], e2[1]-e1[1])
  #find an orthogonal unit vector to create a curved bridge
  #n = 1 or -1 (direction)
  #ax + by = 0, let a = 1 solve for b
  orth_vector = (1, -1*direct_vector[0] / direct_vector[1])
  #divide by magnitude
  m = (orth_vector[0]**2 + orth_vector[1]**2)**0.5
  orth_unit_vector = (n*orth_vector[0]/m, n*orth_vector[1]/m)
  #place the tail at the midpoint
  md_point = ( (e1[0]+e2[0])/2 , (e1[1]+e2[1])/2 )
  return ( md_point[0] + orth_unit_vector[0], md_point[1] + orth_unit_vector[1] )

land_coords = []
bridge_list = []

def build_bridge(e1, e2, w=2):
  #sort by x-coord for simplicity
  if e1[0] > e2[0]:
    e1, e2 = e2, e1

  current_bridges = bridge_list.count((e1,e2))
  if current_bridges == 3:
    print("oops)")
    return False #no more room for bridges!
  elif current_bridges == 0:
    t.setposition(e1[0], e1[1])
    t.pendown()
    t.goto(e2[0],e2[1])
    t.penup()
    bridge_list.append((e1,e2))
  elif current_bridges == 1:
    t.setposition(e1[0], e1[1])
    x, y = get_orth(e1, e2, 1)
    t.pendown()
    t.goto(x*w, y*w)
    t.goto(e2[0], e2[1])
    t.penup()
    bridge_list.append((e1,e2))
  elif current_bridges == 2:
    t.setposition(e1[0], e1[1])
    x, y = get_orth(e1, e2, -1)
    t.pendown()
    t.goto(x*w, y*w)
    t.goto(e2[0], e2[1])
    t.penup()
    bridge_list.append((e1,e2))
  return True

t.penup()
if RANDOM:
  
  for v in range(NUM_LAND):

    x = random.randint(-225,225)
    y = random.randint(-225,225)
    t.setposition(x,y)
    t.dot(10)
    land_coords.append((x,y))

  for e in range(NUM_BRIDGE):

    e1 = e2 = None
    while(e1 == e2):
      e1 = random.choice(land_coords)
      e2 = random.choice(land_coords)

    build_bridge(e1, e2)

    print(bridge_list)
else:
  #rough approximation of Königsberg
  L1 = (0, 200)
  L2 = (200, 0)
  L3 = (0, -200)
  L4 = (-200, 0)

  for L in [L1, L2, L3, L4]:
    t.setposition(L[0], L[1])
    t.dot(10)

  build_bridge(L1, L2)
  build_bridge(L1, L3)
  build_bridge(L1, L4)
  build_bridge(L2, L3)
  build_bridge(L2, L3)
  build_bridge(L3, L4)
  build_bridge(L3, L4)

