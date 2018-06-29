import sys
from turtle import Turtle


class Turn():
    def __init__(self, direction):
        self.direction = direction

    def __invert__(self):
        if self.direction == 'p':
            return Turn('l')
        else:
            return Turn('p')

    def render(self, turtle):
        turtle.forward(3)
        if self.direction == 'p':
            turtle.right(90)
        else:
            turtle.left(90)

def dragon(n):
    result = [Turn('p')]
    for i in range(n):
        new_result = result[:]
        new_result.append(Turn('p'))
        for turn in reversed(result):
            new_result.append(~turn)
        result = new_result
    return result

if __name__ == '__main__':

    d = dragon(10)
    t = Turtle()
    t.speed(0)
    for turn in d:
        turn.render(t)
    input()
