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

	// part 1
	last := -1
	higher := 0
	for _, s := range split {
		i, _ := strconv.Atoi(s)
		if last != -1 && i > last {
			higher++
		}
		last = i
	}
	fmt.Println("Part 1 solution:", higher)

	// part 2
	higher = 0

	lastNums := []int{0, 0, 0}
	lastSum := 0
	for idx, s := range split {
		i, _ := strconv.Atoi(s)

		sum := lastSum + i - lastNums[0]

		lastNums = append(lastNums[1:], i)

		if idx < 3 {
			lastSum = sum
			continue
		}
		if lastSum < sum {
			higher++
		}

		lastSum = sum
	}
	fmt.Println("Part 2 solution:", higher)
}
