import re


def day_2_part_1_answer(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        line_dict = {}
        line_dict['game_number'] = int(re.findall(r"(\d+):", line)[0])
        red_values = [eval(i) for i in re.findall(r"(\d+) red", line)]
        green_values = [eval(i) for i in re.findall(r"(\d+) green", line)]
        blue_values = [eval(i) for i in re.findall(r"(\d+) blue", line)]
        line_dict['max_red'] = max(red_values)
        line_dict['max_green'] = max(green_values)
        line_dict['max_blue'] = max(blue_values)
        if (line_dict['max_red'] <= 12) and (line_dict['max_green'] <= 13) and (line_dict['max_blue'] <= 14):
            total += line_dict['game_number']
    return total


print(day_2_part_1_answer('day2_input.txt'))