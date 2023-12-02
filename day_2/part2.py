import re


def day_2_part_1_answer(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        game_dict = {}
        game_dict['game_number'] = int(re.findall(r"(\d+):", line)[0])
        red_values = [eval(i) for i in re.findall(r"(\d+) red", line)]
        green_values = [eval(i) for i in re.findall(r"(\d+) green", line)]
        blue_values = [eval(i) for i in re.findall(r"(\d+) blue", line)]
        game_dict['max_red'] = max(red_values)
        game_dict['max_green'] = max(green_values)
        game_dict['max_blue'] = max(blue_values)
        power_min_set = game_dict['max_blue']*game_dict['max_green']*game_dict['max_red']
        total += power_min_set

    return total


print(day_2_part_1_answer('day2_input.txt'))