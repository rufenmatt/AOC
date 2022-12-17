open("input.txt") do file
    games = readlines(file)

values = Dict(
    "A"=> 1,
    "B"=> 2,
    "C"=> 3,
    "X"=> 1,
    "Y"=> 2,
    "Z"=> 3
)

win_values = Dict(
    "AX"=> 3,
    "AY"=> 6,
    "AZ"=> 0,
    "BX"=> 0,
    "BY"=> 3,
    "BZ"=> 6,
    "CX"=> 6,
    "CY"=> 0,
    "CZ"=> 3
)

game_sum = 0
game_sum_target = 0

for game in games
    game = split(game, " ")
    result = win_values[game[1]*game[2]]
    game_sum += result + values[game[2]]
end

println("Part 1 solution: $(game_sum)")

game_sum = 0

for game in games
    game = game[1]*game[3]
    if (string(game[2]) == "X")
        for (key, value) in win_values
            if key[1] == game[1] && value == 0
                game_sum += values[string(key[2])]
        end
    end
    elseif (string(game[2]) == "Y")
        for (key, value) in win_values
            if key[1] == game[1] && value == 3
                game_sum += values[string(key[2])] + 3
        end
    end
    elseif (string(game[2]) == "Z")
        for (key, value) in win_values
            if key[1] == game[1] && value == 6
                game_sum += values[string(key[2])] + 6
        end
    end
end

end

println("Part 2 solution: $(game_sum)")

end
