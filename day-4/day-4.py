with open("input.txt", "r") as f:
    lines = f.readlines()
    pairs = [line.strip() for line in lines]

def createSets(pairs):
    left = pairs.split(",")[0]
    leftStart = int(left.split("-")[0].strip())
    leftStop = int(left.split("-")[1].strip())
    leftRange = range(leftStart, leftStop+1)

    right = pairs.split(",")[1]
    rightStart = int(right.split("-")[0].strip())
    rightStop = int(right.split("-")[1].strip())
    rightRange = range(rightStart, rightStop+1)

    return leftRange, rightRange

def part1(pairs):
    counter = 0

    for i in pairs:
        leftRange, rightRange = createSets(i)
        leftSet = set(leftRange)
        rightSet = set(rightRange)

        if leftSet.issubset(rightSet) or rightSet.issubset(leftSet):
            counter +=1

    return counter

def part2(pairs):
    counter = 0

    for i in pairs:
        leftRange, rightRange = createSets(i)
        leftSet = set(leftRange)
        rightSet = set(rightRange)
        overlap = leftSet & rightSet

        if len(overlap)>0:
            counter+=1

    return counter

if __name__ == "__main__":
    print('Part 1 solution:', part1(pairs))
    print('Part 2 solution:', part2(pairs))
