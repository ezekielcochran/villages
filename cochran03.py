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

# def input_villages():
#     print("Enter the total number of villages: ", end = "")
#     village_count = int(input())
#     result = []
#     for i in range(village_count):
#         line = input()
#         result.append(village_string_to_list(line))
#     return result

def input_villages():
    result = [[10, 39, 'mekelle'], [15, 21, 'wukro'], [20, 44, 'adigrat'], [40, 10, 'axum'], [56, 43, 'debre_damo']]
    # result = [[0, 0, 'A'], [3, 3, 'B'], [6, 7, 'C'], [8, 0, 'D'], [11, 6, 'E'], [0, 7, 'F']]
    # result = [0, 0, 'A'], [1000, 500, 'B']
    return result

villages = input_villages()
print(villages)