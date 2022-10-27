###################################
# Student name: Ezekiel Cochran
# Course: COSC 3523 Section 01 - Analysis of Algorithms
# Assignment: #03 - Closest Villages
# Filename: cochran03.py
#
# Purpose: Given a list of 2D points (Villages), find the pair that is closest together
#
# Assumptions: None known
#
# Limitations: Requires specific input: integer followed by lines of two floats and a string each
# 
# Development Computer: 2020 MacBook Pro
# Operating System: macOS Monterey 12.0.1
# Compiler:  none (python)
# Integrated Development Environment (IDE): Visual Studio Code
# Operational Status: Working
###################################

import math

class Village:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    def __str__(self):
        return self.name

class Pair:
    def __init__(self, left, right):
        self.first = left
        self.second = right
        self.distance = distance_between(left, right)
    
    def __str__(self):
        return "{} and {}, distance {}".format(self.first, self.second, self.distance)

def distance_between(a, b):
    x_difference = b.x - a.x
    y_difference = b.y - a.y
    return math.sqrt(x_difference * x_difference + y_difference * y_difference)

def input_villages():
    print("Enter the total number of villages: ", end = "")
    village_count = int(input())
    result = []
    for i in range(village_count):
        line = input().split()
        result.append(Village(float(line[0]), float(line[1]), line[2]))
    return result

def pair_min(first, second):
    if first == None:
        return second
    if second == None:
        return first
    if first.distance > second.distance:
        return second
    else:
        return first

def build_strip(center_x, radius, lower, upper):
    low = center_x - radius
    high = center_x + radius
    center_points = []
    for i in range(lower, upper):
        if low <= villages[i].x <= high:
            center_points.append(villages[i])
    center_points.sort(key = lambda v: v.y)
    return center_points

def smallest_in_strip(strip, radius):
    if len(strip) < 2:
        return None
    best = Pair(strip[0], strip[1])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j].y - strip[i].y < radius:


            this = Pair(strip[i], strip[j])
            if this.distance < best.distance:
                best = this
            j = j + 1
    return best

def recursive_find(li, ri):
    if ri == -1:
        return "There are no villages"
    if li + 1 == ri:
        return Pair(villages[li], villages[ri])
    elif (li == ri):
        return None
    else:
        mi = (li + ri) // 2
        left_min = recursive_find(li, mi)
        right_min = recursive_find(mi + 1, ri)
        sides_min = pair_min(left_min, right_min)
        strip = build_strip(villages[mi].x, sides_min.distance, li, ri + 1)
        strip_best = smallest_in_strip(strip, sides_min.distance)
        return pair_min(sides_min, strip_best)

MAXIMUM_DISTANCE = 1200
villages = input_villages()
villages.sort(key = lambda v: v.x)
solution = recursive_find(0, len(villages) - 1)
if solution.distance <= MAXIMUM_DISTANCE:
    print(solution)
else:
    print("Infeasible")