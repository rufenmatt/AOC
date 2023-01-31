with open("input.txt", "r") as f:
    lines = f.readlines()
    numbers = [int(line.strip()) for line in lines]

def part1(numbers):
    higher = 0
    for i in range(len(numbers)):
        if (numbers[i] > numbers[i-1]):
            higher += 1
    return higher

def part2(numbers):
    higher = 0
    for i in range(len(numbers) - 2):
        if ((numbers[i] + numbers[i+1] + numbers[i+2]) > (numbers[i-1] + numbers[i] + numbers[i+1])):
            higher += 1
    return higher

if __name__ == "__main__":
    print('Part 1 solution:', part1(numbers))
    print('Part 2 solution:', part2(numbers))