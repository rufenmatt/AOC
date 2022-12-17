from dataclasses import dataclass
from typing import Callable, Deque

with open("input.txt", "r") as f:
    lines = f.read()

@dataclass
class Monkey:
    items: Deque[int]
    operation: Callable[[int], int]
    test_divisible: int
    if_true: int
    if_false: int
    inspected_items: int

def get_monkeys(lines, part2):
    monkeys: list[Monkey] = []
    mod = 1

    for block in lines.split("\n\n"):
        lines = block.splitlines()

        items = Deque(map(int, lines[1].split(": ")[1].split(", ")))

        operation = lines[2].split("= ")[1]
        operation = eval(f"lambda old: {operation}")

        test_divisible = int(lines[3].split(" ")[-1])
        if_true = int(lines[4].split(" ")[-1])
        if_false = int(lines[5].split(" ")[-1])

        monkeys.append(Monkey(items, operation, test_divisible, if_true, if_false, 0))
        if part2 == True:
            mod *= test_divisible
        else:
            continue

    return monkeys, mod

def part1(lines):
    monkeys, _ = get_monkeys(lines, part2=False)

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.popleft()

                item = monkey.operation(item)
                item = item // 3

                next_monkey = monkey.if_true if item % monkey.test_divisible == 0 else monkey.if_false
                monkeys[next_monkey].items.append(item)

                monkey.inspected_items += 1

    inspected_items = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)

    return inspected_items[0] * inspected_items[1]

def part2(lines):
    monkeys, mod = get_monkeys(lines, part2=True)

    for _ in range(10000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.popleft()

                item = monkey.operation(item) % mod

                next_monkey = monkey.if_true if item % monkey.test_divisible == 0 else monkey.if_false
                monkeys[next_monkey].items.append(item)

                monkey.inspected_items += 1

    inspected_items = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)

    return inspected_items[0] * inspected_items[1]

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print('Part 2 solution:', part2(lines))
