package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")

	var part1, part2 int
	for _, s := range split[:len(split)] {
		pairs := strings.Split(s, ",")
		left := strings.Split(pairs[0], "-")
		right := strings.Split(pairs[1], "-")
		leftStart, _ := strconv.Atoi(left[0])
		leftEnd, _ := strconv.Atoi(left[1])
		rightStart, _ := strconv.Atoi(right[0])
		rightEnd, _ := strconv.Atoi(right[1])
		if leftStart >= rightStart && leftEnd <= rightEnd {
			part1++
			part2++
			continue
		}
		if leftStart <= rightStart && leftEnd >= rightEnd {
			part1++
			part2++
			continue
		}
		if leftStart >= rightStart && leftStart <= rightEnd {
			part2++
			continue
		}
		if rightStart >= leftStart && rightStart <= leftEnd {
			part2++
			continue
		}
		if leftEnd >= rightStart && leftEnd <= rightEnd {
			part2++
			continue
		}
		if rightEnd >= leftStart && rightEnd <= leftEnd {
			part2++
			continue
		}
	}

	fmt.Println("Part 1 solution:", part1)
	fmt.Println("Part 2 solution:", part2)
}
