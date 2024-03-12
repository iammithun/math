# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:16:14 2024

@author: iamrs
"""

import turtle

def draw_square(color):
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def draw_creeper():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    
    for _ in range(2):
        for _ in range(4):
            draw_square("lime")
            turtle.forward(50)
        turtle.backward(200)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)

    for _ in range(3):
        draw_square("lime")
        turtle.forward(50)
    turtle.backward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    
    draw_square("lime")
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    
    for _ in range(3):
        draw_square("lime")
        turtle.forward(50)
    turtle.backward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    
    for _ in range(2):
        draw_square("lime")
        turtle.forward(50)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

    for _ in range(2):
        draw_square("lime")
        turtle.forward(50)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    
    for _ in range(2):
        draw_square("lime")
        turtle.forward(50)
    turtle.hideturtle()

def main():
    draw_creeper()
    turtle.done()

if __name__ == "__main__":
    main()
