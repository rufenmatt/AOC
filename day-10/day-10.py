with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def part1(lines):
    t = 0
    nxt = 20
    register = 1
    cycle = 0

    for line in lines:
        if line == "noop":
            cycle += 1
        else:
            cycle += 2

        if cycle >= nxt:
            t += nxt * register
            nxt += 40

        if line != "noop":
            register += int(line.split(" ")[1])

    return t

def part2(lines):
    vals = []
    register = 1

    for line in lines:
        if line == "noop":
            vals.append(register)
        else:
            vals.extend([register, register])
            register += int(line.split(" ")[1])

    print('Part 2 solution:')

    for i, val in enumerate(vals):
        pos = i % 40

        if pos in [val - 1, val, val + 1]:
            print("#", end="")
        else:
            print(".", end="")

        if pos == 39:
            print()

    return ""

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print(part2(lines))
