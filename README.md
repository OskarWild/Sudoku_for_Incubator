# Sudoku_for_Incubator
# Игра состоит из 3 уровней сложностей, так же как и обширностей клеток (4*4, 9*9, 16*16). Не полностью доработана, но может показывать ответы и время

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
