package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"
)

var (
	numberPattern   = regexp.MustCompile(`(\d+)`)
	mapNamesPattern = regexp.MustCompile(`(\w+)-to-(\w+) map:`)
)

type Converter struct {
	Seeds   []int64
	Mappers []*Mapper
}

func (c *Converter) String() string {
	return fmt.Sprintf("Seeds: %v, Mappers: %v", c.Seeds, c.Mappers)
}

type MapRange struct {
	DestRangeStart   int64
	SourceRangeStart int64
	RangeLen         int64
}

func (r *MapRange) String() string {
	return fmt.Sprintf("<Dest: %v, Source: %v, Range: %v>", r.DestRangeStart, r.SourceRangeStart, r.RangeLen)
}

type Mapper struct {
	SourceName string
	DestName   string
	Ranges     []*MapRange
}

func (m *Mapper) String() string {
	result := fmt.Sprintf("\n%v-to-%v:", m.SourceName, m.DestName)
	for _, r := range m.Ranges {
		result += "\n" + r.String()
	}
	return result
}

func main() {
	converter := parseFile("day05/day05.dat")

	result1 := int64(math.MaxInt64)
	for _, seed := range converter.Seeds {
		current := seed
		for _, mapper := range converter.Mappers {
			current = mapper.mapSource(current)
		}
		if current < result1 {
			result1 = current
		}
	}
	fmt.Println("Result 1:", result1)

	results := make([]int64, len(converter.Seeds)/2)

	var wg sync.WaitGroup
	for i := 0; i < len(converter.Seeds); i = i + 2 {
		wg.Add(1)

		go func() {
			defer wg.Done()
			results[i/2] = determineSeedRange(converter, i)
		}()
	}

	wg.Wait()
	fmt.Println("Result 2:", slices.Min(results))
}

func determineSeedRange(converter *Converter, idx int) int64 {
	startSeed := converter.Seeds[idx]
	seedRange := converter.Seeds[idx+1]
	fmt.Println("check seed:", startSeed, "at range", seedRange)
	myRes := int64(math.MaxInt64)

	for seed := startSeed; seed < startSeed+seedRange; seed++ {
		current := seed
		for _, mapper := range converter.Mappers {
			current = mapper.mapSource(current)
		}
		if current < myRes {
			myRes = current
		}
	}
	fmt.Println("local Min:", myRes)
	return myRes
}

func parseFile(filename string) *Converter {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	blocks := strings.Split(string(b), "\n\n")
	result := &Converter{}
	for _, block := range blocks {
		lines := strings.Split(block, "\n")
		if len(lines) == 1 { // seeds!
			result.Seeds = extractNumbers(lines[0])
		} else {
			names := mapNamesPattern.FindStringSubmatch(lines[0])
			result.Mappers = append(result.Mappers, &Mapper{
				SourceName: names[1],
				DestName:   names[2],
				Ranges:     parseMapRanges(lines),
			})
		}
	}
	return result
}

func extractNumbers(str string) []int64 {
	result := []int64{}
	for _, s := range numberPattern.FindAllString(str, 1000) {
		n, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		result = append(result, int64(n))
	}
	return result
}

func parseMapRanges(lines []string) []*MapRange {
	result := []*MapRange{}

	for _, l := range lines[1:] {
		ns := extractNumbers(l)
		result = append(result, &MapRange{
			DestRangeStart:   ns[0], // check for correctness!
			SourceRangeStart: ns[1],
			RangeLen:         ns[2],
		})
	}

	return result
}

func (m *Mapper) mapSource(s int64) int64 {
	for _, r := range m.Ranges {
		if r.inRange(s) {
			return s + (r.DestRangeStart - r.SourceRangeStart)
		}
	}
	return s
}

func (r *MapRange) inRange(s int64) bool {
	return s >= r.SourceRangeStart && s < r.SourceRangeStart+r.RangeLen
}
