with open("input.txt", "r") as f:
    lines = f.readlines()
    strings = [line.strip() for line in lines]

def convert_char(chr) -> int:
    return ord(chr.lower()) - ord("a") + (1 if chr.islower() else 27)

def part1(strings):
    total_sum = 0

    for string in strings:
        first = list(string[:int(len(string)/2)])
        second = list(string[-int(len(string)/2):])
        overlay = str(set(first) & set(second))[2]
        total_sum += convert_char((overlay))

    return total_sum

def part2(strings):
    group = []
    total_sum = 0

    for string in strings:
        group.append(string)
        if len(group) == 3:
            overlay = str(set(group[0]) & set(group[1]) & set(group[2]))[2]
            total_sum += convert_char((overlay))
            group = []

    return total_sum

if __name__ == "__main__":
    print('Part 1 solution:', part1(strings))
    print('Part 2 solution:', part2(strings))
