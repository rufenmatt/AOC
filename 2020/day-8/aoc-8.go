package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type instr struct {
	Op  string
	Arg int
}
type instructions []instr

func run(lines instructions) (int, error) {
	accumulator := 0
	seen := make(map[int]bool)
	for i := 0; i < len(lines); i++ {
		_, ran := seen[i]
		if ran {
			return accumulator, errors.New("Already ran.")
		}
		seen[i] = true

		op := lines[i].Op
		arg := lines[i].Arg
		switch op {
		case "jmp":
			i += arg - 1
		case "acc":
			accumulator += arg
		}
	}
	return accumulator, nil
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)
	split := strings.Split(contents, "\n")

	bootcode := make(instructions, 0)
	for i := 0; i < len(split)-1; i++ {
		parts := strings.Fields(split[i])
		arg, _ := strconv.Atoi(parts[1])
		bootcode = append(bootcode, instr{Op: parts[0], Arg: arg})
	}

	accumulator, err := run(bootcode)
	if err != nil {
		fmt.Println("Part 1 solution:", accumulator)
	}

	for i := 0; i <= len(bootcode); i++ {
		op := bootcode[i].Op
		switch op {
		case "jmp":
			bootcode[i].Op = "nop"
		case "nop":
			bootcode[i].Op = "jmp"
		}
		accumulator, err := run(bootcode)
		bootcode[i].Op = op
		if err == nil {
			fmt.Println("Part 2 solution:", accumulator)
			break
		}
	}
}
