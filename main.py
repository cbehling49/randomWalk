"""
Project Name: Random Walk
Author: Cody Behling
Course: CS1400-X01

This program is designed to receive user inputs to determine how random points should be plotted in a turtle window.
The program will also calculate the maximum, minimum, and average distance from start to end.
The program will also output the standard deviation regarding the plotted points' spread.
Users can enter comma-separated values to determine step count.
Users should enter either 100 or 1000 as the value for the number of walk lengths input.
Users can enter the number of trials for which to plot end points.
Users should enter 50 as the value for the number of trials input.
Users can enter one of four walk types (or people) which will determine the points' possible directions.
Users should enter either Pa, Mi-Ma, Reg, or all as the value for the walk type input.
"""

import statistics
import turtle
import random
import math


t = turtle.Turtle()
t.pen(fillcolor='white', pencolor='white')
t.speed(0)

width = 1000
height = 1000


def crow_distance(x, y):
    """calculation for distance as the crow flies"""
    dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
    return dist


def pa(steps, trials):
    """function for pa's random walk"""
    for a in steps:
        newList = []
        d = 1
        d2 = 5
        for c in range(trials):
            x = 0
            y = 0
            x2 = 0
            y2 = 0
            for b in range(a):
                directions = random.randint(1, 4)
                if directions == 1:  # north
                    y += d
                    y2 += d2
                elif directions == 2:  # east
                    x += d
                    x2 += d2
                elif directions == 3:  # south
                    y -= d
                    y2 -= d2
                elif directions == 4:  # west
                    x -= d
                    x2 -= d2
            if a < 1000:
                goto(x2, y2)
                circle()
            cd = crow_distance(x, y)
            newList.append(cd)
        print(f'Pa random walk of {a} steps')
        findTheMax = max(newList)
        findTheMin = min(newList)
        findTheMean = sum(newList) / len(newList)
        findTheCV = (statistics.stdev(newList))
        print(f'Mean = {findTheMean} CV = {findTheCV}')
        print(f'Max = {findTheMax} Min = {findTheMin}')


def mi_ma(steps, trials):
    """function for mi-ma's random walk"""
    for a in steps:
        newList = []
        d = 1
        d2 = 5
        for c in range(trials):
            x = 0
            y = 0
            x2 = 0
            y2 = 0
            for b in range(a):
                directions = random.randint(1, 5)
                if directions == 1:  # north
                    y += d
                    y2 += d2
                elif directions == 2:  # east
                    x += d
                    x2 += d2
                elif directions == 3 or directions == 5:  # south
                    y -= d
                    y2 -= d2
                elif directions == 4:  # west
                    x -= d
                    x2 -= d2
            if a < 1000:
                goto(x2, y2)
                square()
            cd = crow_distance(x, y)
            newList.append(cd)
        print(f'Mi-Ma random walk of {a} steps')
        findTheMax = max(newList)
        findTheMin = min(newList)
        findTheMean = sum(newList) / len(newList)
        findTheCV = (statistics.stdev(newList))
        print(f'Mean = {findTheMean} CV = {findTheCV}')
        print(f'Max = {findTheMax} Min = {findTheMin}')


def reg(steps, trials):
    """function for reg's random walk"""
    for a in steps:
        newList = []
        d = 1
        d2 = 5
        for c in range(trials):
            x = 0
            y = 0
            x2 = 0
            y2 = 0
            for b in range(a):
                directions = random.randint(1, 2)
                if directions == 1:  # east
                    x += d
                    x2 += d2
                elif directions == 2:  # west
                    x -= d
                    x2 -= d2
            if a < 1000:
                goto(x2, y2)
                triangle()
            cd = crow_distance(x, y)
            newList.append(cd)
        print(f'Reg random walk of {a} steps')
        findTheMax = max(newList)
        findTheMin = min(newList)
        findTheMean = sum(newList) / len(newList)
        findTheCV = (statistics.stdev(newList))
        print(f'Mean = {findTheMean} CV = {findTheCV}')
        print(f'Max = {findTheMax} Min = {findTheMin}')


def points(person, steps, trials):
    """user input determines which points are plotted"""
    if person == "Pa":
        pa(steps, trials)
    elif person == "Mi-Ma":
        mi_ma(steps, trials)
    elif person == "Reg":
        reg(steps, trials)
    elif person == "all":
        pa(steps, trials)
        mi_ma(steps, trials)
        reg(steps, trials)


def goto(x, y):
    """allows the turtle to move to another location without drawing a line to get there"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def triangle(side_length=10, fill_color='red'):
    """turtle design for triangle points"""
    t.fillcolor(fill_color)
    t.begin_fill()
    sides = 3
    for i in range(0, sides):
        t.forward(side_length)
        t.left(120)
    t.end_fill()


def square(square_width=10, square_height=10, fill_color='green'):
    """turtle design for square points"""
    t.fillcolor(fill_color)
    t.begin_fill()
    sides = 4
    for i in range(0, sides):
        if (i + 1) % 2 == 0:
            t.forward(square_height)
            t.left(90)
        else:
            t.forward(square_width)
            t.left(90)
    t.end_fill()


def circle(radius=5, fill_color='black'):
    """turtle design for circle points"""
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def main():
    """"""
    try:
        # user inputs
        walk_lengths = input("Enter the walk comma-separated lengths to simulate: ")
        walk_lengths = walk_lengths.split(",")
        for i, walk in enumerate(walk_lengths):
            try:
                walk_lengths[i] = int(walk)
                if walk_lengths[i] < 1:
                    print("Please enter positive integers for walk length.")
            except:
                print("Please enter a valid walk length.")
                return
        walk_trials = input("Enter the number of trials: ")
        try:
            walk_trials = int(walk_trials)
        except:
            print("Please enter a valid trial count.")
            return
        walk_types = input("Enter the name of whomever is walking: ")
        if walk_trials < 1:
            print("Please enter positive integers for trial count.")
        if walk_types != "Pa" and walk_types != "Mi-Ma" and walk_types != "Reg" and walk_types != "all":
            print("Please enter one of the following walk types: Pa, Mi-Ma, Reg, or all")

        # turtle setup
        turtle_screen = turtle.Screen()
        turtle_screen.setup(width + 30, height + 30)
        points(walk_types, walk_lengths, walk_trials)

        print("To exit the program, please click on the screen.")
        turtle_screen.exitonclick()
    except ValueError:
        print("Please enter a valid integer.")
        return


if __name__ == "__main__":
    main()
