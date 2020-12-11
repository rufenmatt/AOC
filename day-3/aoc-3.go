package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func slope_checkin(x int, y int) int {
	tree_count := 0
	currX := 0
	currY := 0
	for currY < len(treeMap)-1 {
		currX = ((x + currX) % len(treeMap[0]))
		currY += y
		tree_count += treeMap[currY][currX]
	}
	return tree_count
}

var treeMap [][]int

func main() {
	dat, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(dat)), "\n")
	treeMap = make([][]int, 0)

	for _, line := range lines {
		treeLine := make([]int, 0)
		for _, d := range line {
			if d == '.' {
				treeLine = append(treeLine, 0)
			} else {
				treeLine = append(treeLine, 1)
			}
		}
		treeMap = append(treeMap, treeLine)
	}
	fmt.Println("Part 1 solution:", slope_checkin(3, 1))
	fmt.Println("Part 2 solution:", slope_checkin(1, 1)*slope_checkin(3, 1)*slope_checkin(5, 1)*slope_checkin(7, 1)*slope_checkin(1, 2))
}
