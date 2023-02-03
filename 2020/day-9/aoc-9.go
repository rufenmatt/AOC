package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var window = flag.Int("window", 25, "The number of entries in the rolling window.")

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)
	split := strings.Split(contents, "\n")
	split = split[:len(split)-1]
	numbers := make([]int, len(split))
	for i, s := range split {
		n, err := strconv.Atoi(s)
		if err != nil {
			fmt.Printf("Failed to parse %s\n", s)
			break
		}
		numbers[i] = n
	}

	var weakness int
	for i, v := range numbers {
		if i < *window {
			continue
		}

		found := false
	middle:
		for n := i - *window; n < i; n++ {
			first := numbers[n]
			if first >= v {
				continue
			}
			for m := n + 1; m < i; m++ {
				second := numbers[m]
				if first+second == v {
					found = true
					break middle
				}
			}
		}
		if !found {
			weakness = v
			break
		}
	}
	fmt.Println("Part 1 solution:", weakness)

	for i, v := range numbers {
		rollingSum := v
		high := v
		low := v
		for n := 1; true; n++ {
			current := numbers[i+n]
			rollingSum += current
			if high < current {
				high = current
			}
			if low > current {
				low = current
			}
			if rollingSum == weakness {
				fmt.Println("Part 2 solution:", high+low)
				return
			}
			if rollingSum > weakness {
				break
			}
		}
	}
}
