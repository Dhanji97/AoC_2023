import re

symbols = [
  '!',
  '@',
  '#',
  '$',
  '%',
  '^',
  '&',
  '*',
  '(',
  ')',
  '-',
  '_',
  '+',
  '=',
  '{',
  '}',
  '[',
  ']',
  '|',
  '\\',
  ';',
  ':',
  "'",
  '"',
  '<',
  '>',
  '?',
  '/',
  ',',
  '`',
  '~'
]

temp = ['467..114..',
        '...*......',
        '..35..633.',
        '......#...', 
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..']

def is_symbol(start_index: int, end_index: int, given_string: str):
    """Returns true if there is a symbol between one before the start index and one after the end index of the given string.
    If the index's fall outside the string, they will revert to the start or end index instead.
    If given string is None will return False"""
    
    if given_string == None:
        return False
    
    start_range = start_index - 1 if start_index - 1 > 0 else start_index
    end_range = end_index + 2 if end_index + 1 < len(given_string) else end_index + 1
    
    for i in range(start_range, end_range):
        if given_string[i] in symbols:
            return True
    else:
        return False

def find_adjacent_numbers(prev_row: str, row: str, next_row: str):
    adjacent_numbers = []
    for number in re.finditer("[0-9]+", row):
        first_index, last_index = number.span()
        last_index = last_index - 1

        #adds number to adjacent_number if there is a symbol before or after the found number on the same row
        symbol_left = first_index - 1 > 0 and row[first_index - 1] != "."
        symbol_right = last_index + 1 < len(row) and row[last_index + 1] != "."
        if symbol_left or symbol_right:
            adjacent_numbers.append(int(number.group(0)))
            continue

        #adds number to adjacent_number if there is a symbol above or below including diagonals
        symbol_above = is_symbol(first_index, last_index, prev_row)
        symbol_below = is_symbol(first_index, last_index, next_row)
        if symbol_above or symbol_below:
            adjacent_numbers.append(int(number.group(0)))
    return adjacent_numbers

def answer(array_string):
    total = 0
    for row_id, row in enumerate(array_string):
        prev_row = array_string[row_id - 1] if row_id - 1 > 0 else None
        next_row = array_string[row_id + 1] if row_id + 1 < len(array_string) else None
        valid_numbers_in_row = find_adjacent_numbers(prev_row, row, next_row)
        for number in valid_numbers_in_row:
            total += number
    return total

with open('day3_input.txt', 'r') as file:
    matrix = [row.strip() for row in file.readlines()]
    print(answer(matrix))