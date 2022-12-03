with open("input.txt", "r") as f:
    lines = f.readlines()
    games = [line.strip() for line in lines]

values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_values = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

def part1(games):
    game_sum = 0

    for game in games:
        game = game.replace(" ", "")
        result = win_values[game[0]+game[1]]
        game_sum += result + values[game[1]]
    return game_sum

def part2(games):
    game_sum = 0

    for game in games:
        game = game.replace(" ", "")
        if game[1] == "X":
            for key, value in win_values.items():
                if key[0] == game[0] and value == 0:
                    game_sum += values[key[1]]
        elif game[1] == "Y":
            for key, value in win_values.items():
                if key[0] == game[0] and value == 3:
                    game_sum += values[key[1]] + 3

        elif game[1] == "Z":
            for key, value in win_values.items():
                if key[0] == game[0] and value == 6:
                    game_sum += values[key[1]] + 6
    return game_sum

if __name__ == "__main__":
    print('Part 1 solution:', part1(games))
    print('Part 2 solution:', part2(games))
