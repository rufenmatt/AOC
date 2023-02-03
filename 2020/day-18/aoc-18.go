package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	data, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer data.Close()
	lines := readInput(data)
	fmt.Printf("Part 1 solution: %d\n", partOne(lines))
	fmt.Printf("Part 2 solution: %d\n", partTwo(lines))
}

func readInput(r io.Reader) []string {
	var lines []string
	input := bufio.NewScanner(r)
	for input.Scan() {
		lines = append(lines, input.Text())
	}
	return lines
}

func partOne(lines []string) int {
	var sum int
	for _, s := range lines {
		sum += evalLine(s)
	}
	return sum
}

func partTwo(lines []string) int {
	var sum int
	for _, s := range lines {
		sum += evalLinePartTwo(s)
	}
	return sum
}

func evalLine(s string) int {
	pos := 0
	return eval(s, &pos)
}

func evalLinePartTwo(s string) int {
	return evalLine(insertParens(s))
}

// from left to right, always increasing pos
func eval(s string, pos *int) int {
	sol := 0
	op := byte('+')
	for {
		var value int
		ch := s[*pos]
		if ch == '(' {
			*pos++
			value = eval(s, pos)
		} else {
			value = int(ch - '0')
		}
		switch op {
		case '+':
			sol += value
		case '*':
			sol *= value
		}
		*pos++
		if *pos >= len(s) || s[*pos] == ')' {
			break
		}
		*pos++
		op = s[*pos]
		*pos += 2
	}
	return sol
}

// parens into the string to reflect the precedence
func insertParens(s string) string {
	for pos := 0; pos < len(s); pos++ {
		if s[pos] == '+' {
			s = parensAround(s, pos)
			pos++
		}
	}
	return s
}

// given a string and the index of a '+', return a string that inserts parens around the two operands
func parensAround(s string, plusIndex int) string {
	var parenDepth, openParen, closeParen int
	// go backwards from the "+" to find where we should put the open paren
	for openParen = plusIndex - 2; openParen > 0; openParen-- {
		switch s[openParen] {
		case ')':
			parenDepth++
		case '(':
			parenDepth--
		}
		if parenDepth == 0 {
			break
		}
	}
	// go forwards from the "+" to find where we should put the close paren
	for closeParen = plusIndex + 2; closeParen < len(s); closeParen++ {
		switch s[closeParen] {
		case ')':
			parenDepth--
		case '(':
			parenDepth++
		}
		if parenDepth == 0 {
			break
		}
	}
	if closeParen == len(s) {
		return s[:openParen] + "(" + s[openParen:] + ")"
	}
	return s[:openParen] + "(" + s[openParen:closeParen+1] + ")" + s[closeParen+1:]
}
