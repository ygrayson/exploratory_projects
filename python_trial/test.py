# test.py
# Qianbo Yin


import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

assert(distance(0, 0, 1, 1) == math.sqrt(2))
