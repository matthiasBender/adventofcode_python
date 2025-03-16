package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

const (
	empty  rune = '.'
	galaxy rune = '#'
)

func main() {
	field := parseFile("day11/day11.dat")
	field = duplicateEmptyCols(field, 1)
	field = duplicateEmptyRows(field, 1)

	galaxies := findCoordinates(field)
	result1 := int64(0)
	for i, g1 := range galaxies {
		for _, g2 := range galaxies[i:] {
			result1 += calcDistance(g1, g2)
		}
	}
	fmt.Println("Result 1:", result1)

	field = parseFile("day11/day11.dat")
	galaxies = findCoordinates(field)
	rows := findEmptyRows(field)
	cols := findEmptyCols(field)

	result2 := int64(0)
	for i, g1 := range galaxies {
		for _, g2 := range galaxies[i:] {
			result2 += calcDistanceWithOffset(g1, g2, [][]int{rows, cols}, 1000000-1)
		}
	}
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) (result [][]rune) {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	for _, line := range strings.Split(string(b), "\n") {
		result = append(result, []rune(line))
	}
	return result
}

func toString(field [][]rune) string {
	result := strings.Builder{}
	for _, row := range field {
		for _, r := range row {
			result.WriteRune(r)
		}
		result.WriteString("\n")
	}
	return result.String()
}

func duplicateEmptyRows(field [][]rune, count int) (result [][]rune) {
	insertRow := make([]rune, len(field[0]))
	for i := range len(field[0]) {
		insertRow[i] = empty
	}
	insertChunk := make([][]rune, count)
	for i := range count {
		insertChunk[i] = insertRow
	}

	for _, row := range field {
		isEmpty := true
		for _, f := range row {
			isEmpty = isEmpty && f == empty
		}
		result = append(result, row)
		if isEmpty {
			result = slices.Concat(result, insertChunk)
		}
	}
	return result
}

func duplicateEmptyCols(field [][]rune, count int) [][]rune {
	insert := make([]rune, count)
	for i := range count {
		insert[i] = empty
	}
	rowCount := len(field)
	result := make([][]rune, rowCount)
	colCount := len(field[0])
	for ic := range colCount {
		isEmpty := true
		for ir := range rowCount {
			isEmpty = isEmpty && field[ir][ic] == empty
			result[ir] = append(result[ir], field[ir][ic])
		}
		if isEmpty {
			for ir := range rowCount {
				result[ir] = slices.Concat(result[ir], insert)
			}
		}
	}
	return result
}

func findCoordinates(field [][]rune) (results [][]int) {
	for ir, row := range field {
		for ic, f := range row {
			if f == galaxy {
				results = append(results, []int{ir, ic})
			}
		}
	}
	return results
}

func findEmptyRows(field [][]rune) (results []int) {
	for i, row := range field {
		isEmpty := true
		for _, r := range row {
			isEmpty = isEmpty && r == empty
		}
		if isEmpty {
			results = append(results, i)
		}
	}
	return results
}

func findEmptyCols(field [][]rune) (results []int) {
	cols := len(field[0])
	for c := range cols {
		isEmpty := true
		for _, row := range field {
			isEmpty = isEmpty && row[c] == empty
		}
		if isEmpty {
			results = append(results, c)
		}
	}
	return results
}

func calcDistance(x, y []int) (result int64) {
	for i := range len(x) {
		result += int64(absDiff(x[i], y[i]))
	}
	return result
}

func calcDistanceWithOffset(x, y []int, empties [][]int, offset int64) (result int64) {
	for i := range len(x) {
		sm := min(x[i], y[i])
		gt := max(x[i], y[i])
		result += int64(gt - sm)
		for _, e := range empties[i] {
			if sm < e && e < gt {
				result += offset
			}
		}
	}

	return result
}

func absDiff(x, y int) int {
	if x > y {
		return x - y
	}
	return y - x
}
