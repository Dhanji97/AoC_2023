example_input = [(7,9), (15,40), (30,200)]
part_1_input = [(50,242),(74,1017),(86,1691),(85,1252)]
part_2_input = [(50748685, 242101716911252)]

def find_lower_time(total_time, distance):
    push_time = 0
    while push_time*(total_time-push_time) <= distance:
        push_time +=1
    return push_time

def find_upper_time(total_time, distance):
    push_time = total_time
    while push_time*(total_time-push_time) <= distance:
        push_time -= 1
    return push_time 

def find_total_number_of_solutions(lower_time, upper_time):
    return (upper_time-lower_time) + 1

def part_1_solution(input_list):
    solution = 1
    for race_tuple in input_list:
        race_time = race_tuple[0]
        target_distance = race_tuple[1]
        smallest_push_time = find_lower_time(race_time, target_distance)
        longest_push_time = find_upper_time(race_time, target_distance)
        race_solutions = find_total_number_of_solutions(smallest_push_time, longest_push_time)
        solution *= race_solutions
    return solution

print(part_1_solution(part_2_input))