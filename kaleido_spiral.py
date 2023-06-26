import turtle


from itertools import cycle
colors = cycle(["red","blue","green","yellow","purple","white","grey"])

def draw_circle(size,angle,shift):
  turtle.pencolor(next(colors))
  turtle.circle(size)
  turtle.right(angle)
  turtle.forward(shift)
  draw_circle(size+2,angle+1,shift+1)


turtle.bgcolor("black")
turtle.speed("fast")
turtle.pensize(4)
draw_circle(10,0,1)





