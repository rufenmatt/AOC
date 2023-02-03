package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

type Rule struct {
	processed string
	subRules  [][]int
}

func ParseRules(rulesSection string) map[int]Rule {
	rules := make(map[int]Rule)
	for _, rule := range strings.Split(strings.TrimSpace(rulesSection), "\n") {
		split := strings.SplitN(rule, ": ", 2)
		ruleContents := split[1]
		rule := Rule{}
		if strings.Contains(ruleContents, "\"") {
			rule.processed = strings.Trim(strings.TrimSpace(ruleContents), "\"")
		} else {
			orMatchers := [][]int{}
			for _, ruleSplit := range strings.Split(ruleContents, "|") {
				splitMatcher := []int{}
				for _, numString := range strings.Split(strings.TrimSpace(ruleSplit), " ") {
					num, _ := strconv.Atoi(numString)
					splitMatcher = append(splitMatcher, num)
				}
				orMatchers = append(orMatchers, splitMatcher)
			}
			rule.subRules = orMatchers
		}

		ruleNum, _ := strconv.Atoi(split[0])
		rules[ruleNum] = rule
	}
	return rules
}

func ResolveRule(rules map[int]Rule, ruleNum int, partTwo bool) string {
	rule := rules[ruleNum]
	if rule.processed != "" {
		return rule.processed
	}
	if partTwo {
		if ruleNum == 8 {
			return ResolveRule(rules, 42, partTwo) + "+"
		} else if ruleNum == 11 {
			rule42 := ResolveRule(rules, 42, partTwo)
			rule31 := ResolveRule(rules, 31, partTwo)
			repeatMatches := []string{}
			for i := 1; i <= 5; i++ {
				repeatMatches = append(repeatMatches, fmt.Sprintf("%s{%d}%s{%d}", rule42, i, rule31, i))
			}
			rule.processed = "(?:" + strings.Join(repeatMatches, "|") + ")"
			return rule.processed
		}
	}
	resolvedParts := []string{}
	for _, orRules := range rule.subRules {
		resolved := []string{}
		for _, linkedRule := range orRules {
			resolved = append(resolved, ResolveRule(rules, linkedRule, partTwo))
		}
		resolvedParts = append(resolvedParts, strings.Join(resolved, ""))
	}
	rule.processed = "(?:" + strings.Join(resolvedParts, "|") + ")"
	return rule.processed
}

func CountMatches(input string, partTwo bool) int {
	sections := strings.Split(input, "\n\n")
	rules := ParseRules(sections[0])
	ruleZero := regexp.MustCompile("^" + ResolveRule(rules, 0, partTwo) + "$")

	matches := 0
	for _, message := range strings.Split(sections[1], "\n") {
		if ruleZero.MatchString(message) {
			matches++
		}
	}
	return matches
}

func PartOne(input string) int {
	return CountMatches(input, false)
}

func PartTwo(input string) int {
	return CountMatches(input, true)
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	contents := string(data)

	fmt.Printf("Part 1 solution: %d\n", PartOne(contents))
	fmt.Printf("Part 2 solution: %d\n", PartTwo(contents))
}
