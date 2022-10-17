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
    # result = [[10, 39, 'mekelle'], [15, 21, 'wukro'], [20, 44, 'adigrat'], [40, 10, 'axum'], [56, 43, 'debre_damo']]
    result = [[0, 0, 'A'], [3, 3, 'B'], [6, 7, 'C'], [8, 0, 'D'], [11, 6, 'E'], [0, 7, 'F']]
    return result

def brute_force(village_list):
    min = MAXIMUM_DISTANCE
    result = []
    for first in village_list:
        for second_index in range(village_list.index(first) + 1, len(village_list)):
            second = village_list[second_index]
            this_distance = distance_between(first, second)
            print("Distance bewtween {} and {} is \t {}".format(first[2], second[2], this_distance))
            if (this_distance < min):
                min = this_distance
                result = [first[2], second[2]]
    if (min == 1200):
        return None
    result.append(min)
    return result


MAXIMUM_DISTANCE = 1200
villages = input_villages()
print(brute_force(villages))