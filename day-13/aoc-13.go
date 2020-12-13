package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

type bus struct {
	position int
	timer    int
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)
	split := strings.Split(contents, "\n")
	timeEstimate, err := strconv.Atoi(split[0])
	timeString := strings.Split(split[1], ",")
	timeInts := []int{}
	for _, time := range timeString {
		if time == "x" {
			continue
		}
		timeInt, err := strconv.Atoi(time)
		if err != nil {
			panic(err)
		}
		timeInts = append(timeInts, timeInt)
	}
	soonest := 0
	bestTime := 1000000000
	for _, testTime := range timeInts {
		remainder := timeEstimate % testTime
		wait := testTime - remainder
		if wait < bestTime {
			bestTime = wait
			soonest = testTime
		}
	}
	fmt.Println("Part 1 solution: ", soonest*bestTime)

	schedules := []bus{}
	for idx, time := range timeString {
		if time == "x" {
			continue
		}
		timeInt, err := strconv.Atoi(time)
		if err != nil {
			panic(err)
		}

		bus := bus{
			position: idx,
			timer:    timeInt,
		}
		schedules = append(schedules, bus)
	}
	sort.SliceStable(schedules, func(i, j int) bool {
		return schedules[i].timer > schedules[j].timer
	})

	i := 1
	internal := 0
	increment := 1
	checkCounter := 0
	for {
		if checkCounter == len(schedules) {
			fmt.Println("Part 2 solution: ", i-increment)
			break
		}
		check := schedules[checkCounter]
		remainder := check.timer - check.position
		if remainder == check.timer {
			remainder = 0
		}
		for remainder < 0 {
			remainder += check.timer
		}
		if i%check.timer == remainder {
			checkCounter++
			internal = 0
			increment = check.timer * increment
		}
		i += increment
		internal++
	}
}
