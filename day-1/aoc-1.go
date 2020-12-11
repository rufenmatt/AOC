package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var nums = make(map[int]bool)

func partOne() int {
	for n := range nums {
		x := 2020 - n
		if _, ok := nums[x]; ok {
			return n * x
		}
	}
	return -1
}

func partTwo() int {
	for n := range nums {
		for m := range nums {
			if n == m {
				continue
			}
			x := 2020 - (n + m)
			_, ok := nums[x]
			if ok {
				return n * m * x
			}
		}
	}
	return -1
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.TrimSpace(string(data))
	for _, line := range strings.Split(lines, "\n") {
		n, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		nums[n] = true
	}
	fmt.Println("Part 1 solution:", partOne())
	fmt.Println("Part 2 solution:", partTwo())
}
