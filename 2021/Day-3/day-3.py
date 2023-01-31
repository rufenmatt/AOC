with open("input.txt", "r") as f:
    lines = f.readlines()
    bits = [line.strip() for line in lines]

def part1(bits):
    zeros = []
    ones = []
    most_common = []
    least_common = []
    initial_list = list(bits[0])

    for i in range(len(initial_list)):
        zeros.append(0)
        ones.append(0)
        most_common.append(0)
        least_common.append(0)

    report = len(bits)

    for i in range(report):
        split_report = list(bits[i])
        for j in range(len(split_report)):
            if split_report[j] == "0":
                zeros[j] += 1
            else:
                ones[j] += 1

    for i in range(len(zeros)):
        if (zeros[i] > ones[i]):
            most_common[i] = "0"
            least_common[i] = "1"
        else:
            most_common[i] = "1"
            least_common[i] = "0"

    most_common_binary = "".join(map(str, most_common))
    least_common_binary = "".join(map(str, least_common))

    return int(most_common_binary, 2) * int(least_common_binary, 2)

def part2(bits):
    lead_zero = 0
    lead_one = 0
    for elem in bits:
        if elem[0] == "0":
            lead_zero += 1
        else:
            lead_one += 1

    if (lead_zero > lead_one):
        most_common = "0"
    else:
        most_common = "1"

    oxygen_generator_numbers = []
    co2_numbers = []

    for elem in bits:
        if elem[0] == most_common:
            oxygen_generator_numbers.append(elem)

        else:
            co2_numbers.append(elem)

    oxygen = helper_oxygen(oxygen_generator_numbers, 1)
    co2 = helper_co2(co2_numbers, 1)

    return int(oxygen, 2) * int(co2, 2)

def helper_co2(bits, idx):
    if len(bits) == 1:
        return bits[0]
    else:
        lead_zero = 0
        lead_one = 0
        for elem in bits:
            if elem[idx] == "0":
                lead_zero += 1
            else:
                lead_one += 1
        if (lead_zero > lead_one):
            most_common = "0"
        else:
            most_common = "1"

        co2_numbers = []
        for elem in bits:
            if elem[idx] == most_common:
                pass
            else:
                co2_numbers.append(elem)

        co2 = helper_co2(co2_numbers, idx + 1)
        return co2

def helper_oxygen(bits, idx):
    if len(bits) == 1:
        return bits[0]
    else:
        lead_zero = 0
        lead_one = 0
        for elem in bits:
            if elem[idx] == "0":
                lead_zero += 1
            else:
                lead_one += 1
        if (lead_zero > lead_one):
            most_common = "0"
        else:
            most_common = "1"

        oxygen_numbers = []
        for elem in bits:
            if elem[idx] == most_common:
                oxygen_numbers.append(elem)
            else:
                pass

        oxygen = helper_oxygen(oxygen_numbers, idx + 1)
        return oxygen

if __name__ == "__main__":
    print('Part 1 solution:', part1(bits))
    print('Part 2 solution:', part2(bits))