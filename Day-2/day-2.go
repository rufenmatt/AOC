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

	horizontal := 0
	vertical := 0
	for _, s := range split {
		elements := strings.Split(s, " ")
		instruction := elements[0]
		maneuver, _ := strconv.Atoi(elements[1])
		switch instruction {
		case "up":
			vertical -= maneuver
		case "down":
			vertical += maneuver
		case "forward":
			horizontal += maneuver
		}
	}
	fmt.Println("Part 1 solution:", horizontal*vertical)

	horizontal = 0
	vertical = 0
	aim := 0
	for _, s := range split {
		elements := strings.Split(s, " ")
		instruction := elements[0]
		maneuver, _ := strconv.Atoi(elements[1])
		switch instruction {
		case "up":
			aim -= maneuver
		case "down":
			aim += maneuver
		case "forward":
			horizontal += maneuver
			vertical += maneuver * aim
		}
	}
	fmt.Println("Part 2 solution:", horizontal*vertical)
}
