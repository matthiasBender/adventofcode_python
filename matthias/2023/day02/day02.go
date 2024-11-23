package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var (
	gamePattern *regexp.Regexp = regexp.MustCompile(`Game (\d+): (.*)$`)
)

type PackageSet struct {
	Red   int
	Blue  int
	Green int
}

type Game struct {
	id   int
	sets []*PackageSet
}

func main() {
	games := parseFile("day02/day02.dat")

	target := &PackageSet{
		Red:   12,
		Blue:  14,
		Green: 13,
	}

	result := 0
	result2 := 0
	for _, game := range games {
		if game.isPossible(target) {
			result += game.id
		}
		result2 += game.maxPackages().power()
	}
	fmt.Println("Result 1:", result)
	fmt.Println("Result 2:", result2)
}

func parseFile(filename string) []*Game {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(b), "\n")
	games := make([]*Game, 0, len(lines))
	for _, line := range lines {
		groups := gamePattern.FindStringSubmatch(line)
		id, _ := strconv.Atoi(groups[1])
		game := &Game{
			id:   id,
			sets: parseSet(groups[2]),
		}
		games = append(games, game)
	}

	return games
}

func parseSet(line string) []*PackageSet {
	result := []*PackageSet{}
	for _, setLine := range strings.Split(line, "; ") {
		newSet := &PackageSet{}
		for _, colorEntry := range strings.Split(setLine, ", ") {
			arr := strings.Split(colorEntry, " ")
			if len(arr) != 2 {
				panic("colorEntry cannot be split!")
			}
			number, _ := strconv.Atoi((arr[0]))
			switch arr[1] {
			case "blue":
				newSet.Blue = number
			case "green":
				newSet.Green = number
			case "red":
				newSet.Red = number
			}
		}
		result = append(result, newSet)
	}
	return result
}

func (g *Game) maxPackages() *PackageSet {
	result := &PackageSet{}
	for _, p := range g.sets {
		if p.Blue > result.Blue {
			result.Blue = p.Blue
		}
		if p.Green > result.Green {
			result.Green = p.Green
		}
		if p.Red > result.Red {
			result.Red = p.Red
		}
	}
	return result
}

func (g *Game) isPossible(allowed *PackageSet) bool {
	maxGame := g.maxPackages()
	return maxGame.Red <= allowed.Red && maxGame.Blue <= allowed.Blue && maxGame.Green <= allowed.Green
}

func (p *PackageSet) power() int {
	return p.Red * p.Blue * p.Green
}
