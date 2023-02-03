package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)
	split := strings.Split(contents, "\n")
	split = strings.Split(split[0], ",")

	a := findNthNumberSpoken(2020, split)
	b := findNthNumberSpoken(30000000, split)

	fmt.Println("Part 1 solution:" + strconv.Itoa(a))
	fmt.Println("Part 2 solution:" + strconv.Itoa(b))
}

func findNthNumberSpoken(n int, input []string) int {
	spoken := make(map[int][]int)

	for i, v := range input {
		n, _ := strconv.Atoi(v)
		spoken[n] = append(spoken[n], i+1)
	}
	prevSpoken := 0
	for j := len(input) + 1; j <= n; j++ {
		var speak int

		if len(spoken[prevSpoken]) < 2 {
			speak = 0
		} else {
			speak = spoken[prevSpoken][1] - spoken[prevSpoken][0]
		}
		if len(spoken[speak]) == 2 {
			spoken[speak] = pop(spoken[speak])
		}
		spoken[speak] = append(spoken[speak], j)
		prevSpoken = speak
	}
	return prevSpoken
}

func pop(a []int) []int {
	_, a = a[0], a[1:]
	return a
}
