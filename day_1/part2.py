number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_front_digit_index(line: str):
    front_pointer = 0
    found_first = False
    while not found_first:
        if line[front_pointer].isdigit():
            return front_pointer, line[front_pointer]
        else:
            front_pointer += 1
            if front_pointer == len(line):
                return float('inf'), None

def find_end_digit_index(line: str):
    end_pointer = -1
    found_last = False
    while not found_last:
        if line[end_pointer].isdigit():
            return (len(line) + end_pointer), line[end_pointer]
        else:
            end_pointer -= 1
            if abs(end_pointer) > len(line):
                return -1, None

def find_first_number_word(line: str):
    earliest_index = float('inf')
    earliest_number = None

    for key in number_dict.keys():
        index = line.find(key)
        if index != -1 and index < earliest_index:
            earliest_index = index
            earliest_number = number_dict[key]

    if earliest_number is not None:
        return earliest_index, earliest_number
    else:
        return float('inf'), None

def find_last_number_word(line:str): 
    latest_index = -1
    latest_number = None

    for key in number_dict.keys():
        index = line.rfind(key)
        if index != -1 and index > latest_index:
            latest_index = index
            latest_number = number_dict[key]

    if latest_number is not None:
        return latest_index, latest_number
    else:
        return -1, None

def answer(txt_file):
    file = open(txt_file, 'r')
    Lines = [line.strip() for line in file.readlines()]
    total_value = 0

    for line in Lines:

        front_digit_index, front_digit_element = find_front_digit_index(line)
        front_word_index, front_word_element = find_first_number_word(line)
        if front_digit_index < front_word_index:
            first_number = front_digit_element
        else:
            first_number = front_word_element

        last_digit_index, last_digit_element = find_end_digit_index(line)
        last_word_index, last_word_element = find_last_number_word(line)
        if last_digit_index > last_word_index:
            last_number = last_digit_element
        else:
            last_number = last_word_element
        line_value = int(first_number + last_number)
        total_value += line_value

    return total_value

aws = answer('day1_text.txt')
print(aws)
