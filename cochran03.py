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
    result = [[10, 39, 'mekelle'], [15, 21, 'wukro'], [20, 44, 'adigrat'], [40, 10, 'axum'], [56, 43, 'debre_damo']]
    return result

villages = input_villages()
print(villages)