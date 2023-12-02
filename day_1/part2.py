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


def find_digit(line: str, from_front: bool = True):
    """A function that finds the first digit in a given string. It will return the index of the digit and the digit found, as a string.
    The function will search from the front of the string when from_front is true or not provided, if no digit is found an infinite float and None is returned.
    The function will search from the back of the string when fro_front is False, if no digit is found -1 and None are returned."""
    string_len = len(line)
    index_array = range(string_len) if from_front else reversed(range(string_len))
    for i in index_array:
        if line[i].isdigit():
            return i, line[i]
    if from_front:
        print ('flag 1')
        return float('inf'), None
    else:
        return -1, None


def find_number_word(line: str, from_front: bool = True):
    """A function that finds the first number in english for a given string. It will return the index of the number and the digit of the number found as a string.
    The function will search from the front of the string when from_front is true or not provided, if no number is found an infinite float and None is returned.
    The function will search from the back of the string when from_front is False, if no number is found -1 and None are returned."""
    index_func = line.find if from_front else line.rfind
    index_value = float('inf') if from_front else -1
    result_index = index_value
    result_number = None

    for key in number_dict.keys():
        index = index_func(key)
        if index != -1:
            if (from_front and index < result_index) or (not from_front and index > result_index):
                result_index = index
                result_number = number_dict[key]

    if result_number is not None:
        return result_index, result_number
    else:
        return index_value, None


def evaluate_first_index(index_1: float or int, number_1: str, index_2: float or int, number_2: str, is_smallest: bool = True):
    """A function that compares the index of the from the numbers found in the string and returns the number with the required condition.
    If is_smallest is True or not provided it will compare for the smallest index, i.e. the index that is closest to the start.
    if is_smallest is False it will compare to find the biggest index, i.e. the index that is closest to the end. """
    if (is_smallest and index_1 < index_2) or (not is_smallest and index_1 > index_2 ):
        return number_1
    else:
        return number_2

def day_1_part_2_answer(txt_file):
    file = open(txt_file, 'r')
    Lines = [line.strip() for line in file.readlines()]
    total_value = 0

    for line in Lines:
        front_digit_index, front_digit_element = find_digit(line)
        front_word_index, front_word_element = find_number_word(line)

        last_digit_index, last_digit_element = find_digit(line, False)
        last_word_index, last_word_element = find_number_word(line, False)

        first_number = evaluate_first_index(front_digit_index, front_digit_element, front_word_index, front_word_element)
        last_number = evaluate_first_index(last_digit_index, last_digit_element, last_word_index, last_word_element, False)

        line_value = int(first_number + last_number)
        total_value += line_value

    return total_value


answer = day_1_part_2_answer('day1_text.txt')
print(answer)
