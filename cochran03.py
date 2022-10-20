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
        return "{} and {}, distance {}".format(self.first.name, self.second.name, self.distance)

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
        result.append(Village(int(line[0]), int(line[1]), line[2]))
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

villages = input_villages()
villages.sort(key = lambda v: v.x)

hail_mary = recursive_find(0, len(villages) - 1)
print(hail_mary)