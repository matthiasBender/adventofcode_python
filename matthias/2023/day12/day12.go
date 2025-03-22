package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

const (
	broken      = '#'
	operational = '.'
	unknown     = '?'
)

type Row struct {
	springs []rune
	blocks  []int
}

func main() {
	rows := parseFile("day12/day12.dat")
	result1 := int64(0)
	for _, r := range rows {
		result1 += matchNumbers(r.springs, r.blocks, make(map[string]int64))
	}
	fmt.Println("Result 1:", result1)

	result2 := int64(0)
	for _, r := range rows {
		r.unfold(5)
		result2 += matchNumbers(r.springs, r.blocks, make(map[string]int64))
	}

	fmt.Println("Result 2:", result2)
}

func matchNumbers(springs []rune, blocks []int, cache map[string]int64) int64 {
	springslen := len(springs)

	if len(blocks) == 0 {
		if slices.Contains(springs, broken) {
			return 0
		}
		return 1
	}

	if c, ok := cache[toCacheKey(springs, blocks)]; ok {
		return c
	}

	block := blocks[0]
	startPos := []int{}
SPRINGS:
	for i, spring := range springs {
		switch spring {
		case broken:
			startPos = append(startPos, i)
			break SPRINGS
		case unknown:
			startPos = append(startPos, i)
		}
	}

	totalCount := int64(0)
	for _, sp := range startPos {
		matches := true
		for bp := range block {
			if sp+bp >= springslen || springs[sp+bp] == operational {
				matches = false
				break
			}
		}
		currentPos := sp + block
		if matches && (currentPos == springslen || springs[currentPos] == operational || springs[currentPos] == unknown) {
			sps := springs[min(springslen, currentPos+1):]
			bls := blocks[1:]
			newCount := matchNumbers(sps, bls, cache)
			cache[toCacheKey(sps, bls)] = newCount
			totalCount += newCount
		}
	}

	return totalCount
}

func toCacheKey(springs []rune, blocks []int) string {
	return (&Row{springs: springs, blocks: blocks}).String()
}

func (r *Row) unfold(x int) {
	springs := make([]rune, 0, len(r.springs)*x+x)
	blocks := make([]int, 0, len(r.blocks)*x)
	for i := range x {
		if i > 0 {
			springs = append(springs, unknown)
		}
		springs = append(springs, r.springs...)
		blocks = append(blocks, r.blocks...)
	}
	r.springs = springs
	r.blocks = blocks
}

func parseFile(filename string) (result []*Row) {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	for _, line := range strings.Split(string(b), "\n") {
		parts := strings.Split(line, " ")
		blocks := []int{}
		for _, ns := range strings.Split(parts[1], ",") {
			n, err := strconv.Atoi(ns)
			if err != nil {
				panic(err)
			}
			blocks = append(blocks, n)
		}
		result = append(result, &Row{
			springs: []rune(parts[0]),
			blocks:  blocks,
		})
	}

	return result
}

func (r *Row) String() string {
	result := string(r.springs) + " "
	ns := make([]string, len(r.blocks))
	for i, n := range r.blocks {
		ns[i] = strconv.Itoa(n)
	}
	return result + strings.Join(ns, ",")
}
