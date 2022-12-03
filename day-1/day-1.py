with open("input.txt", "r") as f:
    lines = f.readlines()
    numbers = [line.strip() for line in lines]

def count_calories(numbers):
    calories_held = []
    calories = 0
    for i in numbers:
        if i:
            calories += int(i)
        else:
            calories_held.append(calories)
            calories = 0

    calories_held.append(calories)

    return calories_held

def part1(x):
    return max(x)

def part2(x):
    return sum(sorted(x)[-3:])

if __name__ == "__main__":
    print('Part 1 solution:', part1(count_calories(numbers)))
    print('Part 2 solution:', part2(count_calories(numbers)))
