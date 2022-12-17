with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def get_grid(lines):
    grid = []

    for line in lines:
        grid.append([int(ch) for ch in line])

    width = len(grid[0])
    height = len(grid)

    return grid, width, height

def part1(lines):
    grid, width, height = get_grid(lines)
    t = 0

    for y in range(height):
        for x in range(width):
            if y == 0 or x == 0 or y == height - 1 or x == width - 1:
                t += 1
            else:
                row = grid[y]
                col = [row[x] for row in grid]
                val = grid[y][x]

                if max(row[:x]) < val or max(row[x+1:]) < val or max(col[:y]) < val or max(col[y+1:]) < val:
                    t += 1

    return t

def part2(lines):
    grid, width, height = get_grid(lines)
    max_score = 0

    for y in range(height):
        for x in range(width):
            score = 1

            t = 0
            for i in range(x - 1, -1, -1):
                t += 1
                if grid[y][i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(x + 1, width):
                t += 1
                if grid[y][i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y - 1, -1, -1):
                t += 1
                if grid[i][x] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y + 1, height):
                t += 1
                if grid[i][x] >= grid[y][x]:
                    break
            score *= t

            max_score = max(max_score, score)

    return max_score

if __name__ == "__main__":
    print('Part 1 solution:', part1(lines))
    print('Part 2 solution:', part2(lines))
