with open("input.txt", "r") as f:
    lines = f.readlines()
    pairs = [line.strip() for line in lines]

def createSets(pairs):
    left = pairs.split(",")[0]
    left_start = int(left.split("-")[0].strip())
    left_stop = int(left.split("-")[1].strip())
    left_range = range(left_start, left_stop+1)

    right = pairs.split(",")[1]
    left_stop = int(right.split("-")[0].strip())
    right_stop = int(right.split("-")[1].strip())
    right_range = range(left_stop, right_stop+1)

    return left_range, right_range

def part1(pairs):
    counter = 0

    for i in pairs:
        left_range, right_range = createSets(i)
        left_set = set(left_range)
        right_set = set(right_range)

        if left_set.issubset(right_set) or right_set.issubset(left_set):
            counter +=1

    return counter

def part2(pairs):
    counter = 0

    for i in pairs:
        left_range, right_range = createSets(i)
        left_set = set(left_range)
        right_set = set(right_range)
        overlap = left_set & right_set

        if len(overlap)>0:
            counter+=1

    return counter

if __name__ == "__main__":
    print('Part 1 solution:', part1(pairs))
    print('Part 2 solution:', part2(pairs))
