import turtle
import random

######################
# This code is a demonstration of the Seven Bridges of Königsberg problem
# the field of Graph Theory began here!
# Read more: https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
######################

NUM_LAND = 4
NUM_BRIDGE = 7
#Change these to alter the number of bridges and city sections
RANDOM = False
#Change this to True to get a random layout
EXAMPLE_CODE = True
#Change this to False to run your own code

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

def draw_bridge(e1, e2, n, w=2):
#draws a path between two nodes, takes a curve if straight path already exists
    t.setposition(e1[0], e1[1])
    t.pendown()
    if n == 1:
      x, y = get_orth(e1, e2, 1)
      t.goto(x*w, y*w)
    elif n == 2:
      x, y = get_orth(e1, e2, -1)

    t.goto(e2[0],e2[1])
    t.penup()

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

  draw_bridge(e1, e2, current_bridges)
  bridge_list.append((e1,e2))
  return True

t.penup()
if RANDOM:
#randomly generate a city layout, may or may not contain an Euler Path
  print("placing city sections")  
  for v in range(NUM_LAND):

    x = random.randint(-225,225)
    y = random.randint(-225,225)
    t.setposition(x,y)
    t.dot(10)
    land_coords.append((x,y))

  print("building bridges")
  for e in range(NUM_BRIDGE):

    e1 = e2 = None
    while(e1 == e2):
      e1 = random.choice(land_coords)
      e2 = random.choice(land_coords)

    build_bridge(e1, e2)

    #print(bridge_list)
else:

  #rough approximation of Königsberg
  L1 = (0, 200)
  L2 = (200, 0)
  L3 = (0, -200)
  L4 = (-200, 0)

  for L in [L1, L2, L3, L4]:
    land_coords.append(L)
    t.setposition(L[0], L[1])
    t.dot(10)

  build_bridge(L1, L2)
  build_bridge(L1, L3)
  build_bridge(L1, L4)
  build_bridge(L2, L3)
  build_bridge(L2, L3)
  build_bridge(L3, L4)
  build_bridge(L3, L4)

  #uncomment to make an Euler path
  #build_bridge(L2, L4)
  #NUM_BRIDGE += 1

def dfs(edges, node, path):
  #attempt to find an Euler path

  neighbors = [ i for i in range(NUM_LAND) if edges[node][i] ]
  if neighbors:
    for n in neighbors:

      edges[node][n] -= 1
      edges[n][node] -= 1

      path.append(n)

      if not dfs(edges, n, path):
        edges[node][n] += 1
        edges[n][node] += 1
        path.pop()
      else:
        return True
      return False
  else:

    if sum([sum(edges[n]) for n in range(NUM_LAND)]) == 0:
      print("path found")
      return True
    return False


def run():
  path = []
  edges = [[0]*NUM_LAND for n in land_coords]

  for b in bridge_list:
    edges[land_coords.index(b[0])][land_coords.index(b[1])] += 1
    edges[land_coords.index(b[1])][land_coords.index(b[0])] += 1

  #print(edges)
  if EXAMPLE_CODE:

    if dfs(edges, 0, path):
      #trace the found Euler path
      t.color("red", "red")
      t.shape("turtle")
      t.setposition(land_coords[0][0], land_coords[0][1])
      t.showturtle()
      t.pendown()
      node = 0
      for p in path:
        current_bridges = edges[node][p]
        draw_bridge(land_coords[node], land_coords[p], current_bridges)
        edges[node][p] += 1
        edges[p][node] += 1
        node = p
    else:
      print("no path")
      t.setposition(0,0)
      t.write("no path found", align="center", font=("Arial", 24, "normal"))
  else:
    pass
#####################
# Here is where you can
# Write some code
# Of your very own
#####################

run()
