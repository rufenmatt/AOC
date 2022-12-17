import copy

with open("input.txt", "r") as f:
    lines = f.readlines()

movements_lines = False
stacks = []

for crates in lines:
    if not crates.replace(" ", "").strip():
        movements_lines = True
        continue
    if not movements_lines:
        stacks.append(crates)

box_stack = [[] for _ in range(len(stacks[0].replace(" ", ""))-1)]

for i in range(len(stacks[0].replace(" ", ""))-2):
    row = lines[i].split(" ")
    row_formated = []
    j = 0
    while j < len(row):
        if row[j] == "":
            j += 4
            row_formated.append("")
        else:
            row_formated.append(row[j][1])
            j += 1
    for i, box in enumerate(row_formated):
        if box:
            box_stack[i].insert(0, box)

def part1():
    box_stack_copy = copy.deepcopy(box_stack)
    for i in range(len(stacks[0].replace(" ", "")), len(lines)):
        move_nums = [int(i) for i in lines[i].split() if i.isdigit()]
        num, num_move_from, num_move_to = [int(x) for x in move_nums]

        for _ in range(num):
            box_stack_copy[num_move_to - 1].append(box_stack_copy[num_move_from - 1].pop())

    return "".join([x[-1] for x in box_stack_copy])


def part2():
    box_stack_copy = copy.deepcopy(box_stack)
    for i in range(len(stacks[0].replace(" ", "")), len(lines)):
        move_nums = [int(i) for i in lines[i].split() if i.isdigit()]
        num, num_move_from, num_move_to = [int(x) for x in move_nums]

        box_stack_copy[num_move_to - 1].extend(box_stack_copy[num_move_from - 1][-num:])
        box_stack_copy[num_move_from - 1] = box_stack_copy[num_move_from - 1][:-num]

    return "".join([x[-1] for x in box_stack_copy])


if __name__ == "__main__":
    print('Part 1 solution:', part1())
    print('Part 2 solution:', part2())