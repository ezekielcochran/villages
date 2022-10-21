import math
import time
import random

class Village:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    def __str__(self):
        return self.name

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.distance = distance_between(first, second)
    
    def __str__(self):
        return "{} and {}, distance {}".format(self.first.name, self.second.name, self.distance)

class Space:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
    
    def __str__(self):
        return "x between {} and {}, y between {} and {}".format(self.min_x, self.max_x, self.min_y, self.max_y)

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
    # for i in range(len(strip)): # DELETE THESE TWO LINES ONCE WE KNOW THE ALTERNATIVE WORKS
    #     for j in range(i + 1, min(7, len(strip))):
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
        
def prebuilt_villages():
    result = [Village(10, 39, 'mekelle'), Village(15, 21, 'wukro'), Village(20, 44, 'adigrat'), Village(40, 10, 'axum'), Village(56, 43, 'debre_damo')]
    # result = [Village(0, 0, 'A'), Village(3, 3, 'B'), Village(6, 7, 'C'), Village(8, 0, 'D'), Village(11, 6, 'E'), Village(0, 7, 'F')]
    return result

def class_brute():
    min = Pair(villages[0], villages[1])
    for first in villages:
        for second in villages[villages.index(first) + 1::]:
            this = Pair(first, second)
            if this.distance < min.distance:
                min = this
    return min

def verify(tent):
    check = class_brute()
    if check.distance != tent.distance:
        return False
    if check.first == tent.first and check.second == tent.second:
        return True
    if check.first == tent.second and check.second == tent.first:
        return True
    return False

def build(num_points, s):
    result = []
    for i in range(num_points):
        this = Village(random.uniform(s.min_x, s.max_x), random.uniform(s.min_y, s.max_y), "city " + str(i))
        result.append(this)
    return result

village_count = 10000

random.seed(1)

MAXIMUM_DISTANCE = 1200
continent = Space(0, MAXIMUM_DISTANCE, 0, MAXIMUM_DISTANCE)
# villages = build(village_count, continent)
# villages = input_villages()
# start_time = time.time_ns()
# villages.sort(key = lambda v: v.x)
# fast_answer = recursive_find(0, len(villages) - 1)
# end_time = time.time_ns()
# runtime = (end_time - start_time) / 1000000000
# print("\nFast answer: {}".format(fast_answer), end = "\t\t\t")
# print("Runtime:     {}".format(runtime))
# start_time = time.time_ns()
# print("Verify:      {}".format(class_brute()), end = "\t\t\t")
# end_time = time.time_ns()
# runtime = (end_time - start_time) / 1000000000
# print("Verify time: {}\n".format(runtime))

results_filename = "runtimes.txt"
# all_true = True
output = open(results_filename, "w")
for i in range(100, 300001, 10000):
    print(i, end = "\t")
    villages = build(i, continent)
    start_time = time.time_ns()
    villages.sort(key = lambda x:x.x)
    fast_answer = recursive_find(0, len(villages) - 1)
    print(fast_answer, end = "\t")
    end_time = time.time_ns()
    runtime = (end_time - start_time) / 1000000000
    # brute_start = time.time_ns()
    # verified = verify(fast_answer)
    # brute_end = time.time_ns()
    # brute_runtime = (brute_end - brute_start) / 1000000000
    # if not verified:
        # all_true = False
    # print(verified, end = "\t")
    print(runtime)
    # output.write("{}, {}, {}\n".format(i, runtime, brute_runtime))
    output.write("{}, {}\n".format(i, runtime))
output.close()
# print("\nAll searches were correct: {}\nResults written to \"{}\"".format(all_true, results_filename))
print("\nResults unchecked\nResults written to \"{}\"".format(results_filename))