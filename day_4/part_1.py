
with open('day_4_input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    total = 0
    for line in lines:
        line_without_card_number = line.split(':')[1]
        winning_and_scratched_numbers_list = line_without_card_number.split('|')
        winning_numbers = [int(num) for num in winning_and_scratched_numbers_list[0].strip().split()]
        scratched_numbers = [int(num) for num in winning_and_scratched_numbers_list[1].strip().split()]
        matched_number_count = 0
        for number in winning_numbers:
            if number in scratched_numbers:
                matched_number_count += 1
        line_value = 2**(matched_number_count - 1) if matched_number_count > 0 else 0
        total += line_value
    print(total)