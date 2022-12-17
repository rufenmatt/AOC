with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = lines[0]

def part1(lines):
    for i in range(4, len(lines)):
        if len(set(lines[i-4:i])) == 4:
            return i

def part2(lines):
    for i in range(4, len(lines)):
        if len(set(lines[i-14:i])) == 14:
            return i

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print('Part 2 solution:', part2(lines))
