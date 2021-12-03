def part_one_solution(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    w, h = 2, 12
    bit_array = [[0 for x in range(w)] for y in range(h)] 

    for line in lines:
        for index, char in enumerate(line):
            if index < len(line)-1:
                if char == "0":
                    bit_array[index][0] += 1
                else:
                    bit_array[index][1] += 1


    gamma_rate = ""
    epsilon_rate = ""

    for list in bit_array:
        if list[0] > list[1]:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
        else:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"

    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    return gamma_rate_dec * epsilon_rate_dec


def part_two_solution(input_file):
    with open(input_file) as f:
        lines = f.readlines()
    
    vals = []

    for line in lines:
        line = line.strip()
        vals.append(line)

    oxygen_filtered = vals
    co2_filtered = vals

    for i in range(12):
        oxygen_filtered = filter(oxygen_filtered, i, "most_common")

    for i in range(12):
        co2_filtered = filter(co2_filtered, i, "least_common")
    
    return int(oxygen_filtered[0],2) * int(co2_filtered[0],2)
    


def filter(vals, index, option):

    if len(vals) == 1:
        return vals 

    bits = [0, 0]

    for val in vals:
        if val[index] == "0":
            bits[0] += 1
        else:
            bits[1] += 1
    
    filtered_vals = []
    if option == "most_common":
        if bits[0] > bits[1]:
            for val in vals:
                if val[index] == "0":
                    filtered_vals.append(val)
        if bits[0] <= bits[1]:
            for val in vals:
                if val[index] == "1":
                    filtered_vals.append(val)

    if option == "least_common":
        if bits[0] > bits[1]:
            for val in vals:
                if val[index] == "1":
                    filtered_vals.append(val)
        if bits[0] <= bits[1]:
            for val in vals:
                if val[index] == "0":
                    filtered_vals.append(val)
    
    return filtered_vals



answer = part_one_solution("input.txt")
print answer

answer = part_two_solution("input.txt")
print answer