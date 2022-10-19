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

def input_villages(): # This is the part of the main branch I would like to keep the same
    print("Enter the total number of villages: ", end = "")
    village_count = int(input())
    result = []
    for i in range(village_count):
        line = input()
        result.append(village_string_to_list(line))
    return result # To here

villages = input_villages()