"""This program uses python's turtle module to provide a key events that enables the user to draw patterns on the screen
This was programmed by JBAmenorfe on the 9th January 2025"""

from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

# Define the functions that will provide the actions to be performed by each key
## A funcitonthat moves the turtle forward
def move_forward():
    tim.forward(10)

## A function that moves the turtle backward
def move_backward():
    tim.backward(10)

## A function that moves the turtle anticlockwise
def turn_left():
    tim.left(10)

## A function that moves the turtle clockwise
def turn_right():
    tim.right(10)

## A function to clear the drawings on the screen
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.setheading(0)
    tim.pendown()

screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(turn_right, key="a")
screen.onkey(turn_left, key="d")
screen.onkey(clear_screen, key="c")

screen.exitonclick()