def part_one_solution(input_file):
    count = 0
    with open(input_file) as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        if index < len(lines)-1:
            if int(line) < int(lines[index+1]):
                count += 1
    
    return count


def part_two_solution(input_file):
    count = 0
    with open(input_file) as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        if index < len(lines)-3:
            window_sum = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
            next_window_sum = int(lines[index+1]) + int(lines[index+2]) + int(lines[index+3])
            if window_sum < next_window_sum:
                count += 1

    return count



part_one_answer = part_one_solution('input.txt')
part_two_answer = part_two_solution('input.txt')

print ('Part One answer: {} \nPart Two answer: {}'.format(part_one_answer, part_two_answer))