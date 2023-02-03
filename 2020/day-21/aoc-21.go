package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type alergen = string
type ingredient = string

type food struct {
	ingredients []ingredient
	alergens    []alergen
}

func sliceToMap(strings []string) map[string]bool {
	result := make(map[string]bool)
	for _, s := range strings {
		result[s] = true
	}
	return result
}

func getSomeKey(m map[string]bool) string {
	var result string
	for s := range m {
		result = s
		break
	}
	return result
}

func partOne(foods []food) (int, map[alergen]ingredient) {
	canBeIn := make(map[alergen](map[ingredient]bool))

	for _, food := range foods {
		for _, a := range food.alergens {
			foodIngredients := sliceToMap(food.ingredients)

			if allergenPossibilities, seen := canBeIn[a]; seen {
				for i := range allergenPossibilities {
					if _, ok := foodIngredients[i]; !ok {
						delete(allergenPossibilities, i)
					}
				}
			} else {
				canBeIn[a] = foodIngredients
			}
		}
	}

	assignment := make(map[alergen]ingredient)
	fixedIngredients := make(map[ingredient]bool)

	for len(canBeIn) > 0 {
		found := false

		for a, possibilities := range canBeIn {
			if len(possibilities) == 1 {
				i := getSomeKey(possibilities)
				assignment[a] = i
				fixedIngredients[i] = true

				delete(canBeIn, a)
				for _, l := range canBeIn {
					delete(l, i)
				}

				found = true
				break
			}
		}

		if !found {
			panic("Failed to uniquely assign; more general approach needed. :(")
		}
	}

	result := 0
	for _, food := range foods {
		for _, i := range food.ingredients {
			if _, isFixed := fixedIngredients[i]; !isFixed {
				result++
			}
		}
	}

	return result, assignment
}

func partTwo(assignment map[alergen]ingredient) string {
	var alergens []alergen
	for a := range assignment {
		alergens = append(alergens, a)
	}

	sort.Strings(alergens)

	var dangerous []ingredient
	for _, a := range alergens {
		dangerous = append(dangerous, assignment[a])
	}
	return strings.Join(dangerous, ",")
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var foods []food

	for scanner.Scan() {
		line := scanner.Text()
		splits := strings.Split(line, " (")

		foods = append(foods,
			food{strings.Split(splits[0], " "),
				strings.Split(splits[1][9:len(splits[1])-1], ", ")},
		)
	}

	pOne, assingment := partOne(foods)
	fmt.Printf("Part 1 solution: %d\n", pOne)
	fmt.Printf("Part 2 solution: %s\n", partTwo(assingment))
}
