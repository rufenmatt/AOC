open("input.txt") do file
    lines = readlines(file)

    calories_held = 0
    calories = 0
    for line in lines
        if(line != "")
            calories += parse(Int, line)
        elseif(calories > calories_held)
            calories_held = calories
            calories = 0
        else
            calories = 0
        end
    end
    if(calories > calories_held)
        calories_held = calories
    end

    println("Part 1 solution: $(calories_held)")

    calories_held = Vector{Int64}()
    calories = 0
    for line in lines
        if(line != "")
            calories += parse(Int, line)
        else
            append!(calories_held, calories)
            calories = 0
        end
    end
    append!(calories_held, calories)
    println("Part 2 solution: $(sum(first(sort!(calories_held, rev = true), 3)))")
end
