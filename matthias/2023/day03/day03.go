package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	gear rune = 42
)

var (
	numberPattern = regexp.MustCompile(`(\d+)`)
	nonSymbols    = map[rune]bool{
		48: true,
		49: true,
		50: true,
		51: true,
		52: true,
		53: true,
		54: true,
		55: true,
		56: true,
		57: true,
		46: true,
	}
)

type PartNumber struct {
	Number int
	Row    int
	Start  int
	End    int
}

type Symbol struct {
	c   rune
	Row int
	Col int
}

func main() {
	partNumbers, symbols := parseFile("day03/day03.dat")

	result := 0
	for _, num := range partNumbers {
		if num.contactsAnySymbol(symbols) {
			result += num.Number
		}
	}
	fmt.Println("Result 1:", result)

	result2 := 0
	for _, g := range findGears(symbols) {
		result2 += g.validateGear(partNumbers)
	}
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) ([]*PartNumber, []*Symbol) {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")
	result := []*PartNumber{}
	resultSymbols := []*Symbol{}
	for row, line := range lines {
		numbers := numberPattern.FindAllString(line, 10000)
		positions := numberPattern.FindAllStringIndex(line, 10000)
		for i, num := range numbers {
			n, _ := strconv.Atoi(num)
			result = append(result, &PartNumber{
				Number: n,
				Row:    row,
				Start:  positions[i][0],
				End:    positions[i][1],
			})
		}
		for col, c := range line {
			if _, ok := nonSymbols[c]; !ok {
				resultSymbols = append(resultSymbols, &Symbol{
					c:   c,
					Row: row,
					Col: col,
				})
			}
		}
	}
	return result, resultSymbols
}

func (num *PartNumber) contactsAnySymbol(symbols []*Symbol) bool {
	for _, sym := range symbols {
		if num.contactsSymbol(sym) {
			return true
		}
	}
	return false
}

func (num *PartNumber) contactsSymbol(sym *Symbol) bool {
	return sym.Row >= num.Row-1 && sym.Row <= num.Row+1 && sym.Col >= num.Start-1 && sym.Col <= num.End
}

func findGears(symbols []*Symbol) []*Symbol {
	result := []*Symbol{}
	for _, sym := range symbols {
		if sym.c == gear {
			result = append(result, sym)
		}
	}
	return result
}

func (sym *Symbol) validateGear(numbers []*PartNumber) int {
	ratio := 1
	found := 0
	for _, num := range numbers {
		if num.contactsSymbol(sym) {
			found += 1
			ratio *= num.Number
		}
	}
	if found != 2 {
		return 0
	}
	return ratio
}
