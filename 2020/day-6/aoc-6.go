package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)
	split := strings.Split(contents, "\n")
	split = split[:len(split)-1]
	groupNumber := 0
	groups := []map[rune]int{
		make(map[rune]int),
	}
	groupSize := []int{0}
	for _, s := range split {
		if s == "" {
			groups = append(groups, make(map[rune]int))
			groupSize = append(groupSize, 0)
			groupNumber++
			continue
		}
		for _, r := range s {
			groups[groupNumber][r]++
		}
		groupSize[groupNumber]++
	}
	sum := 0
	yes := 0
	for n, g := range groups {
		sum += len(g)
		for _, count := range g {
			if count == groupSize[n] {
				yes++
			}
		}
	}
	fmt.Println("Part 1 solution:", sum)
	fmt.Println("Part 2 solution:", yes)
}
