def part_one_solution(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    horizontal_position = 0
    depth = 0

    for line in lines:
        if "forward" in line:
            x = int(line.strip("forward"))
            horizontal_position += x
        elif "down" in line:
            x = int(line.strip("down"))
            depth += x
        elif "up" in line:
            x = int(line.strip("up"))
            depth -= x

    return horizontal_position * depth


def part_two_solution(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for line in lines:
        if "down" in line:
            x = int(line.strip("down"))
            aim += x
        if "up" in line:
            x = int(line.strip("up"))
            aim -= x
        if "forward" in line:
            x = int(line.strip("forward"))
            depth += x * aim
            horizontal_position += x          
    
    return horizontal_position * depth


part_one_answer = part_one_solution('input.txt')
part_two_answer = part_two_solution('input.txt')

print ('Part One answer: {} \nPart Two answer: {}'.format(part_one_answer, part_two_answer))