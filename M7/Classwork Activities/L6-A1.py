import turtle

sc = turtle.Screen()
# creating canvas 
sc.bgcolor("pink")

sc.setup(500, 500)

turtle.title("Welcome to Turtle Window")

# turtle object creation 
board = turtle.Turtle()

n = 8
# creating a square
for i in range(n):
    board.forward(100)
    board.left(360/n)

turtle.done()