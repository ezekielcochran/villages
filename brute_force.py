import math

def village_string_to_list(input_line):
    line_list = input_line.split()
    line_list[0] = int(line_list[0])
    line_list[1] = int(line_list[1])
    return line_list

def distance_between(a, b):
    x_difference = b[0] - a[0]
    y_difference = b[1] - a[1]
    return math.sqrt(x_difference * x_difference + y_difference * y_difference)

def input_villages():
    print("Enter the total number of villages: ", end = "")
    village_count = int(input())
    result = []
    for i in range(village_count):
        line = input()
        result.append(village_string_to_list(line))
    return result

def brute_force(village_list):
    min = 1200
    result = []
    for first in village_list:
        for second in village_list:
            this_distance = distance_between(first, second)
            if (this_distance < min and first != second):
                min = this_distance
                result = [first[2], second[2]]
    if (min == 1200):
        return None
    result.append(min)
    return result



villages = input_villages()
print(brute_force(villages))