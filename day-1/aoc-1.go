package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	entries := readData("input.txt")

	{
		fmt.Println("Part 1 solution")
	one:
		for _, a := range entries {
			for _, b := range entries {
				if a+b == 2020 {
					fmt.Println(a * b)
					break one
				}
			}
		}
	}

	{
		fmt.Println("Part 2 solution")
	two:
		for _, a := range entries {
			for _, b := range entries {
				for _, c := range entries {
					if a+b+c == 2020 {
						fmt.Println(a * b * c)
						break two
					}
				}
			}
		}
	}
}

func readData(filename string) []int {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	var values []int
	for scanner.Scan() {
		values = append(values, Int(scanner.Text()))
	}
	return values
}

func Int(s string) int {
	result, err := strconv.Atoi(s)
	check(err)
	return result
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}
