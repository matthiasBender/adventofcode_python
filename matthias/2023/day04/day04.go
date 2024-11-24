package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var (
	numberPattern = regexp.MustCompile(`(\d+)`)
)

type Card struct {
	Number  int
	Winning []int
	Got     []int
	Won     int
}

func main() {
	cards := parseFile("day04/day04.dat")
	result1 := 0
	for _, card := range cards {
		result1 += card.points()
	}
	fmt.Println("Result 1:", result1)

	result2 := 0
	for ic, card := range cards {
		ms := card.matches()
		for i := 1; i <= ms && i+ic < len(cards); i++ {
			cards[ic+i].Won += card.Won
		}
		result2 += card.Won
	}
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) []*Card {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	cards := []*Card{}
	for cardNum, line := range strings.Split(string(b), "\n") {
		halves := strings.Split(strings.Split(line, ": ")[1], " | ")
		cards = append(cards, &Card{
			Number:  cardNum + 1,
			Winning: extractNumbers(halves[0]),
			Got:     extractNumbers(halves[1]),
			Won:     1,
		})
	}
	return cards
}

func extractNumbers(str string) []int {
	result := []int{}
	for _, s := range numberPattern.FindAllString(str, 1000) {
		n, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		result = append(result, n)
	}
	return result
}

func (c *Card) points() int {
	result := 0
	for _, n := range c.Got {
		for _, w := range c.Winning {
			if n == w {
				if result == 0 {
					result = 1
				} else {
					result *= 2
				}
				break
			}
		}
	}
	return result
}

func (c *Card) matches() int {
	result := 0
	for _, n := range c.Got {
		for _, w := range c.Winning {
			if n == w {
				result += 1
				break
			}
		}
	}
	return result
}
