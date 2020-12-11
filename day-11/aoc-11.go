package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const FLOOR = '.'
const EMPTY = 'L'
const TAKEN = '#'

func neighbors(seats [][]byte, i, j, visibilityRange int) int {
	res := 0
	directions := [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	for _, d := range directions {
		ni, nj := i+d[0], j+d[1]
		steps := 1
		for 0 <= ni && ni <= len(seats)-1 &&
			0 <= nj && nj <= len(seats[0])-1 {
			if seats[ni][nj] == EMPTY {
				break
			}
			if seats[ni][nj] == TAKEN {
				res++
				break
			}
			if visibilityRange != -1 && steps >= visibilityRange {
				break
			}
			ni += d[0]
			nj += d[1]
			steps++
		}
	}
	return res
}

func show(seats [][]byte) {
	for _, s := range seats {
		fmt.Println(string(s))
	}
	fmt.Println()
}

func nextState(seats [][]byte, tolerance, visibilityLimit int) ([][]byte, bool) {
	modified := false
	rows, cols := len(seats), len(seats[0])
	new := make([][]byte, rows)
	for i := range new {
		new[i] = make([]byte, cols)
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			new[i][j] = seats[i][j]
			if seats[i][j] == FLOOR {
				continue
			}
			neighbors := neighbors(seats, i, j, visibilityLimit)
			if seats[i][j] == EMPTY && neighbors == 0 {
				new[i][j] = TAKEN
				modified = true
			}
			if seats[i][j] == TAKEN && neighbors >= tolerance {
				new[i][j] = EMPTY
				modified = true
			}
		}
	}
	return new, modified
}

func occSeatsStabilized(seats [][]byte, tolerance, visibilityLimit int) int {
	seats, modified := nextState(seats, tolerance, visibilityLimit)
	for modified {
		seats, modified = nextState(seats, tolerance, visibilityLimit)
	}

	res := 0
	for _, line := range seats {
		for _, seat := range line {
			if seat == TAKEN {
				res++
			}
		}
	}
	return res
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	text := strings.TrimSpace(string(data))
	seats := [][]byte{}
	for _, line := range strings.Split(text, "\n") {
		seats = append(seats, []byte(line))
	}
	fmt.Println("Part 1 solution:", occSeatsStabilized(seats, 4, 1))
	fmt.Println("Part 2 solution:", occSeatsStabilized(seats, 5, -1))
}
