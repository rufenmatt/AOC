import os

os.getcwd()

os.chdir(r'/Users/mattiarufenacht/Desktop/AOC2021/Day-2')

with open("input.txt", "r") as f:
    lines = f.readlines()
    maneuver = [line.strip() for line in lines]

def part1(maneuver):
    vertical = 0
    horizontal = 0
    for elem in maneuver:
        instruction = elem.split()[0]
        maneuver = int(elem.split()[1])
        if instruction == "down":
            vertical += maneuver
        elif instruction == "up":
            vertical -= maneuver
        elif instruction == "forward":
            horizontal += maneuver

    return vertical*horizontal

def part2(maneuver):
    vertical = 0
    horizontal = 0
    aim = 0
    for elem in maneuver:
        instruction = elem.split()[0]
        maneuver = int(elem.split()[1])
        if instruction == "down":
            aim += maneuver
        elif instruction == "up":
            aim -= maneuver
        elif instruction == "forward":
            horizontal += maneuver
            vertical = (aim * maneuver) + vertical

    return vertical * horizontal

if __name__ == "__main__":
    print('Part 1 solution:', part1(maneuver))
    print('Part 2 solution:', part2(maneuver))