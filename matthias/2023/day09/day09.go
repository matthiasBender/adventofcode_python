package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	sequences := parseFile("day09/day09.dat")

	result1 := int64(0)
	result2 := int64(0)
	for _, s := range sequences {
		seqs := genUntilZero(s)
		result1 += int64(extrapolate(seqs))
		result2 += int64(extrapolateBack(seqs))
	}
	fmt.Println("Result 1:", result1)
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) [][]int {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	result := [][]int{}
	for _, line := range strings.Split(string(b), "\n") {
		row := []int{}
		for _, token := range strings.Split(line, " ") {
			n, err := strconv.Atoi(token)
			if err != nil {
				panic(err)
			}
			row = append(row, n)
		}
		result = append(result, row)
	}
	return result
}

func genUntilZero(seq []int) [][]int {
	result := [][]int{}
	for last := seq; !isZeros(last); last = subtract(last) {
		result = append(result, last)
	}
	result = append(result, make([]int, len(result[len(result)-1])-1))
	return result
}

func subtract(seq []int) []int {
	result := make([]int, len(seq)-1)
	for i := 1; i < len(seq); i++ {
		result[i-1] = seq[i] - seq[i-1]
	}
	return result
}

func isZeros(seq []int) bool {
	result := true
	for _, val := range seq {
		result = result && val == 0
	}
	return result
}

func extrapolate(seqs [][]int) int {
	result := 0
	for _, s := range seqs {
		result += s[len(s)-1]
	}
	return result
}

func extrapolateBack(seqs [][]int) int {
	result := 0
	for i := len(seqs) - 2; i >= 0; i-- {
		result = seqs[i][0] - result
	}

	return result
}
