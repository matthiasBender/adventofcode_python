package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type HandType string

const (
	typeFive      = HandType("7five-of-a-kind")
	typeFour      = HandType("6four-of-a-kind")
	typeFull      = HandType("5full-house")
	typeThree     = HandType("4three-of-a-kind")
	typeTwoPair   = HandType("3two-pair")
	typePair      = HandType("2pair")
	typeHigh      = HandType("1high-card")
	cardOrdering  = "23456789TJQKA"
	cardOrderingJ = "J23456789TQKA"
	joker         = rune(74)
)

type Hand struct {
	cards string
	bet   int
}

func (h *Hand) String() string {
	return h.cards + " " + strconv.Itoa(h.bet)
}

func main() {
	hands := parseFile("day07/day07.dat")

	sort.Slice(hands, func(i, j int) bool { return !hands[i].isGreater(hands[j]) })
	result1 := 0
	for rank, hand := range hands {
		result1 += (rank + 1) * hand.bet
	}
	fmt.Println("Result 1:", result1)

	sort.Slice(hands, func(i, j int) bool { return !hands[i].isGreaterJ(hands[j]) })
	result2 := 0
	for rank, hand := range hands {
		result2 += (rank + 1) * hand.bet
	}
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) []*Hand {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	result := []*Hand{}
	for _, line := range strings.Split(string(b), "\n") {
		parts := strings.Split(line, " ")
		bet, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		result = append(result, &Hand{
			cards: parts[0],
			bet:   bet,
		})
	}
	return result
}

func (h *Hand) getType() HandType {
	cardMap := make(map[rune]int)
	for _, c := range h.cards {
		cardMap[c] += 1
	}

	switch len(cardMap) {
	case 1:
		return typeFive
	case 2:
		for _, count := range cardMap {
			if count == 1 || count == 4 { // we can immediately decide which one it is since there only two entries
				return typeFour
			}
			return typeFull
		}
	case 3:
		for _, count := range cardMap {
			if count == 3 {
				return typeThree
			}
		}
		return typeTwoPair
	case 4:
		return typePair
	}
	return typeHigh
}

func (h *Hand) getTypeJ() HandType {
	cardMap := make(map[rune]int)
	for _, c := range h.cards {
		cardMap[c] += 1
	}
	maxN := 0
	maxC := rune(65) // start with an 'A'
	for c, n := range cardMap {
		if c != joker && n > maxN {
			maxN = n
			maxC = c
		}
	}
	cardMap[maxC] += cardMap[joker]
	delete(cardMap, joker)

	switch len(cardMap) {
	case 1:
		return typeFive
	case 2:
		for _, count := range cardMap {
			if count == 1 || count == 4 { // we can immediately decide which one it is since there only two entries
				return typeFour
			}
			return typeFull
		}
	case 3:
		for _, count := range cardMap {
			if count == 3 {
				return typeThree
			}
		}
		return typeTwoPair
	case 4:
		return typePair
	}
	return typeHigh
}

func (h1 *Hand) isGreater(h2 *Hand) bool {
	t1 := h1.getType()
	t2 := h2.getType()
	if t1 == t2 {
		for i, c1 := range h1.cards {
			c2 := rune(h2.cards[i])
			if c1 != c2 {
				return strings.IndexRune(cardOrdering, c1) > strings.IndexRune(cardOrdering, c2)
			}
		}
	}
	return t1 > t2
}

func (h1 *Hand) isGreaterJ(h2 *Hand) bool {
	t1 := h1.getTypeJ()
	t2 := h2.getTypeJ()
	if t1 == t2 {
		for i, c1 := range h1.cards {
			c2 := rune(h2.cards[i])
			if c1 != c2 {
				return strings.IndexRune(cardOrderingJ, c1) > strings.IndexRune(cardOrderingJ, c2)
			}
		}
	}
	return t1 > t2
}
