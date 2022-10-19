import math

def max_name_length(list):
    max = len(list[0][2])
    for i in range(2, len(list)):
        this_length = len(list[i][2])
        if this_length > max:
            max = this_length
    return max

def pad (list):
    length = max_name_length(list)
    print("LENGTH: {}".format(length))
    for town in list:
        name = town[2]
        while len(name) != length:
            name = name + "-"
        # print(name + "|")
        town[2] = name

def village_string_to_list(input_line):
    line_list = input_line.split()
    line_list[0] = int(line_list[0])
    line_list[1] = int(line_list[1])
    return line_list

def distance_between(a, b):
    x_difference = b[0] - a[0]
    y_difference = b[1] - a[1]
    # return math.sqrt(x_difference * x_difference + y_difference * y_difference)
    return x_difference * x_difference + y_difference * y_difference

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
    if (min == MAXIMUM_DISTANCE):
        return None
    result.append(min)
    return result


MAXIMUM_DISTANCE = 1200
villages = input_villages()
pad(villages)
solution = brute_force(villages)
if solution == None:
    output = "There are no villages within {max_distance} miles of each other.".format(max_distance = MAXIMUM_DISTANCE)
else:
    solution[2] = math.sqrt(solution[2])
    output = "The closest villages are {0[0]} and {0[1]}, which are {0[2]:.2f} miles apart.".format(solution)
print("\n"*2)
print(output)