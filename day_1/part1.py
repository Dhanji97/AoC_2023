
file = open('day1_text.txt', 'r')
Lines = file.readlines()

total_value = 0
for line in Lines:
    front_pointer = 0
    end_pointer = -1
    found_first = False
    found_last = False
    while not found_first:
        if line[front_pointer].isdigit():
            front_number = line[front_pointer]
            found_first = True
        else:
            front_pointer += 1
    while not found_last:
        if line[end_pointer].isdigit():
            end_number = line[end_pointer]
            found_last = True
        else:
            end_pointer -= 1
    line_value = int(front_number+end_number)
    total_value += line_value

print(total_value)

