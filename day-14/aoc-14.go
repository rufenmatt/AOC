package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func partOne(inputString []string) int {
	mem := make(map[int]int64, 0)
	mask := ""
	for _, l := range inputString {
		parts := strings.Split(l, "=")
		if len(parts) < 2 {
			continue
		}

		if strings.TrimSpace(parts[0]) == "mask" {
			mask = strings.TrimSpace(parts[1])
		} else {
			add := strings.TrimSpace(parts[0])
			add = strings.ReplaceAll(add, "mem[", "")
			add = strings.ReplaceAll(add, "]", "")
			address, _ := strconv.Atoi(add)
			num, _ := strconv.Atoi(strings.TrimSpace(parts[1]))
			binary := strconv.FormatInt(int64(num), 2)

			mem[address] = applyMaskOne(mask, binary)
		}
	}
	ans := 0
	for v := range mem {
		ans += int(mem[v])
	}

	return ans
}

func applyMaskOne(mask string, binary string) int64 {
	res := ""

	for i := len(mask) - 1; i >= 0; i-- {
		diff := len(mask) - i - 1
		c := "0"
		if diff < len(binary) {
			c = string(binary[len(binary)-diff-1])
		}

		if string(mask[i]) != "X" {
			c = string(mask[i])
		}

		res = c + res
	}

	num, _ := strconv.ParseInt(res, 2, 64)

	return num
}

func partTwo(inputString []string) int {
	mem := make(map[string]int, 0)
	mask := ""
	for _, l := range inputString {
		parts := strings.Split(l, "=")
		if len(parts) < 2 {
			continue
		}

		if strings.TrimSpace(parts[0]) == "mask" {
			mask = strings.TrimSpace(parts[1])
		} else {
			add := strings.TrimSpace(parts[0])
			add = strings.ReplaceAll(add, "mem[", "")
			add = strings.ReplaceAll(add, "]", "")
			address, _ := strconv.Atoi(add)

			binaryAddress := strconv.FormatInt(int64(address), 2)
			genAddr := applyMaskTwo(mask, binaryAddress)
			num, _ := strconv.Atoi(strings.TrimSpace(parts[1]))

			for v := range genAddr {
				mem[genAddr[v]] = int(num)
			}
		}
	}

	ans := 0
	for v := range mem {
		ans += int(mem[v])
	}

	return ans
}

// If the bitmask bit is 0, the memory address bit = unchanged.
// If the bitmask bit is 1, the memory address bit = overwritten with 1.
// If the bitmask bit is X, the memory address bit = is floating.
func applyMaskTwo(mask string, binary string) []string {
	res := ""

	for i := len(mask) - 1; i >= 0; i-- {
		diff := len(mask) - i - 1
		c := "0"
		if diff < len(binary) {
			c = string(binary[len(binary)-diff-1])
		}

		if string(mask[i]) == "X" {
			c = string(mask[i])
		} else if string(mask[i]) == "1" {
			c = "1"
		}

		res = c + res
	}

	gen := generateAddrs([]string{res})

	return gen
}

// addresses based on floating indexes
func generateAddrs(addresses []string) []string {
	done := true

	for i, addr := range addresses {
		for c := 0; c < len(addr); c++ {
			if string(addr[c]) == "X" {
				done = false
				addr1 := addr[0:c] + "0" + addr[c+1:]
				addr2 := addr[0:c] + "1" + addr[c+1:]

				addresses = append(addresses[:i], addresses[i+1:]...)

				addresses = append(addresses, addr1)
				addresses = append(addresses, addr2)

				return generateAddrs(addresses)
			}
		}
	}

	if done {
		return addresses
	}

	return []string{}
}

func main() {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	inputString := strings.Split(strings.TrimSpace(string(data)), "\n")

	ans := partOne(inputString)
	fmt.Println("Part 1 solution:", ans)

	ans = partTwo(inputString)
	fmt.Println("Part 2 solution:", ans)
}
