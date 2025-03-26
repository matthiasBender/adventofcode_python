package main

import (
	"fmt"
	"os"
	"strings"
)

type Block struct {
	lines  []string
	width  int
	height int
}

func main() {
	blocks := parseFile("day13/day13.dat")

	result1 := 0
	for _, block := range blocks {
		result1 += block.findRow() * 100
		result1 += block.transpose().findRow()
		fmt.Println("ROWS:", block.findRow())
		fmt.Println("COLS:", block.transpose().findRow(), "\n")
	}
	fmt.Println("Result 1:", result1)
}

func (b *Block) findRow() int {
	rowsLower := b.lines[:b.height-1]
	rowsUpper := b.lines[1:]
	candidates := []int{}
	for i, rl := range rowsLower {
		if rl == rowsUpper[i] {
			candidates = append(candidates, i)
		}
	}
	if len(candidates) == 0 {
		return 0
	}
	for _, c := range candidates {
		if c == 0 || c == b.height-2 { // no further comparissons needed
			return c + 1
		}
		isMirror := true

		counter := min(c, b.height-c-2)
		for lc := range counter {
			isMirror = isMirror && b.lines[c-1-lc] == b.lines[c+2+lc]
		}

		if isMirror {
			return c + 1
		}
	}

	return 0
}

func parseFile(filename string) []*Block {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	result := []*Block{}
	for _, block := range strings.Split(string(b), "\n\n") {
		lines := strings.Split(block, "\n")
		result = append(result, &Block{
			lines:  lines,
			width:  len(lines[0]),
			height: len(lines),
		})
	}
	return result
}

func (b *Block) String() string {
	return strings.Join(b.lines, "\n")
}

func (b *Block) transpose() *Block {
	builders := make([]strings.Builder, b.width)
	for _, line := range b.lines {
		for i, r := range line {
			builders[i].WriteRune(r)
		}
	}
	result := make([]string, 0, b.width)
	for _, b := range builders {
		result = append(result, b.String())
	}

	return &Block{
		height: b.width,
		width:  b.height,
		lines:  result,
	}
}
