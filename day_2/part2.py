import re


def day_2_part_1_answer(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        red_values = [eval(i) for i in re.findall(r"(\d+) red", line)]
        green_values = [eval(i) for i in re.findall(r"(\d+) green", line)]
        blue_values = [eval(i) for i in re.findall(r"(\d+) blue", line)]
        max_red = max(red_values)
        max_green = max(green_values)
        max_blue = max(blue_values)
        power_min_set = max_blue*max_green*max_red
        total += power_min_set

    return total


print(day_2_part_1_answer('day2_input.txt'))