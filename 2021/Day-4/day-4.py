with open("input.txt", "r") as f:
    lines = f.readlines()
    numbers = [line.strip() for line in lines]

def part1(numbers):
    numbers_drawn = list(numbers[0].split(","))
    grid_list = []
    for i in range(1, len(numbers)):
        if not numbers[i]:
            grid_list.append([])
        else:
            grid_list[-1].append((numbers[i].split()))

    for number_drawn in numbers_drawn:
        for grid in grid_list:
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] == number_drawn:
                        grid[i][j] = "X"

        for grid in grid_list:
            if victorious_grid(grid) == True:
                board_sum = get_board_sum(grid)
                return board_sum * int(number_drawn)

def victorious_grid(checked_grid):
    for line in checked_grid:
        interim_sum = 0
        for i in range(len(line)):
            if line[i].isdigit():
                interim_sum += int(line[i])
        if interim_sum == 0:
            return True

    for i in range(len(checked_grid)):
        interim_sum = 0
        for j in range(len(checked_grid)):
            if checked_grid[j][i].isdigit():
                interim_sum += int(checked_grid[j][i])
        if interim_sum == 0:
            return True
    return False

def get_board_sum(checked_grid):
    interim_sum = 0
    for i in range(len(checked_grid)):
        for j in range(len(checked_grid)):
            if checked_grid[i][j].isdigit():
                interim_sum += int(checked_grid[i][j])
    return interim_sum

def part2(numbers):
    drawn_numbers = list(numbers[0].split(","))
    grids_list = []
    winning_grids_list = []

    for i in range(1, len(numbers)):
        if not numbers[i]:
            grids_list.append([])
        else:
            grids_list[-1].append((numbers[i].split()))

    for x in range(len(drawn_numbers)):
        for grid in grids_list:
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] == drawn_numbers[x]:
                        grid[i][j] = "X"


        for grid in grids_list:
            if victorious_grid(grid) == True:
                if grid not in winning_grids_list:
                    winning_grids_list.append(grid)

            if (len(winning_grids_list)) == len(grids_list) - 1:
                for grid in grids_list:
                    if victorious_grid(grid) != True:
                        for i in range(len(grid)):
                            for j in range(len(grid)):
                                if grid[i][j] == drawn_numbers[x + 1]:
                                    grid[i][j] = "X"
                        board_sum = get_board_sum(grid)

                return board_sum * int(drawn_numbers[x + 1])


if __name__ == "__main__":
    print('Part 1 solution:', part1(numbers))
    print('Part 2 solution:', part2(numbers))
