package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	example = `
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`
	example2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
)

var (
	keys = []string{
		"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
	}
	digits = map[string]int{
		"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
)

func main() {
	result := 0
	result2 := 0
	data := readFile()
	// data := example2
	for _, line := range strings.Split(data, "\n") {
		first, last := findFirstAndLastDigit(line)
		result += 10*first + last
		first2, last2 := findFirstLast(line)
		result2 += 10*first2 + last2
	}
	fmt.Println("Result Part1:", result)
	fmt.Println("Result Part2:", result2)
}

func findFirstAndLastDigit(str string) (first int, last int) {
	foundFirst := false
	for _, c := range str {
		i, err := strconv.Atoi(string(c))
		if err == nil {
			if !foundFirst {
				foundFirst = true
				first = i
			}
			last = i
		}
	}
	return first, last
}

func readFile() string {
	b, err := os.ReadFile("day01/day01.dat")
	if err != nil {
		panic(err)
	}

	return string(b)
}

func findFirstLast(line string) (int, int) {
	firstIndex := len(line)
	lastIndex := -1
	firstValue := 0
	lastValue := 0

	for _, key := range keys {
		if i := strings.Index(line, key); i >= 0 && i < firstIndex {
			firstIndex = i
			firstValue = digits[key]
		}
		if i := strings.LastIndex(line, key); i > lastIndex {
			lastIndex = i
			lastValue = digits[key]
		}
	}
	return firstValue, lastValue
}
