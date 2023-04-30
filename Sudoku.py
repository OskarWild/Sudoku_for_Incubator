import turtle
import random
import math
import time
import os

best_result = 0 
start_time = time.time()

wn = turtle.Screen()
wn.setup(600, 600)
wn.title('Sudoku for NFactorial')
wn.tracer(0)

timer_pen = turtle.Turtle()
timer_pen.pencolor('yellow')
timer_pen.hideturtle()
timer_pen.penup()

finish = False
moll = True
class TheGame:
    def __init__(self, n = 9, missing = 0, demo = True):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.unsolved_board = []
        self.srn = int(math.sqrt(n))
        self.missing = missing
        self.demo = demo
        self.timer = time.time()

    def fill_box(self, row, col):
        num = [i for i in range(1, self.n + 1)]
        for i in range(self.srn):
            for j in range(self.srn):
                x = random.choice(num)
                num.remove(x)
                self.board[row + i][col + j] = x

    def diagonal(self):
        for i in range(0, self.n, self.srn):
            self.fill_box(i, i)

    def possible(self, number, row, column):
        global board
        for i in range(0, n):
            if self.board[row][i] == number:
                return False
        for i in range(0, n):
            if self.board[i][column] == number:
                return False
        x0 = (column // self.srn) * self.srn
        y0 = (row // self.srn) * self.srn
        for i in range(0,self.srn):
            for j in range(0,self.srn):
                if self.board[y0 + i][x0 + j] == number:
                    return False

        return True

 