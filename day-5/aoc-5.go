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
	split = split[:len(split)-1]
	highestSeat := 0
	var seen [1024]bool
	for _, s := range split {
		if len(s) != (7 + 3) {
			fmt.Printf("Invalid boarding pass length: %s\n", s)
		}
		bits := strings.ReplaceAll(s, "B", "1")
		bits = strings.ReplaceAll(bits, "R", "1")
		bits = strings.ReplaceAll(bits, "F", "0")
		bits = strings.ReplaceAll(bits, "L", "0")
		val, err := strconv.ParseInt(bits, 2, 0)
		if err != nil {
			fmt.Printf("Failed to parse %s\n", bits)
		}
		value := int(val)
		seen[value] = true
		if value > highestSeat {
			highestSeat = value
		}
	}
	fmt.Println("Part 1 solution:", highestSeat)
	init := true
	for i, found := range seen {
		if init && found {
			init = false
			continue
		}
		if !init && !found {
			fmt.Println("Part 2 solution:", i)
			break
		}
	}
}
