package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

const (
	empty  byte = 0
	round  byte = 1
	blocky byte = 2
)

type Rock struct {
	x int
	y int
}

type Field struct {
	fields [][]byte
	rocks  []*Rock
}

func main() {
	field := parseFile("day14/day14.dat")
	t := time.Now()
	for field.moveNorth() {
	}
	elapsed := time.Since(t)
	fmt.Println("Result 1:", field.calculateLoad(), elapsed)

	field = parseFile("day14/day14.dat")

	t = time.Now()
	finalI := -1
	seen := map[string]int{field.String(): 0}
	for i := range 1000000000 {
		field.cylcle()
		asString := field.String()
		if when, ok := seen[asString]; ok {
			finalI = (1000000000 - 1 - when) % (i - when)
			break
		}
		seen[asString] = i
	}
	for _ = range finalI {
		field.cylcle()
	}
	fmt.Println("Result 2:", field.calculateLoad(), time.Since(t))
}

func (f *Field) cylcle() {
	for f.moveNorth() {
	}
	for f.moveWest() {
	}
	for f.moveSouth() {
	}
	for f.moveEast() {
	}
}

func (f *Field) moveNorth() bool {
	moved := false
	for _, rock := range f.rocks {
		if rock.x > 0 && f.fields[rock.x-1][rock.y] == empty {
			f.fields[rock.x][rock.y] = empty
			rock.x--
			f.fields[rock.x][rock.y] = round
			moved = true
		}
	}
	return moved
}

func (f *Field) moveSouth() bool {
	moved := false
	maxSouth := len(f.fields) - 1
	for _, rock := range f.rocks {
		if rock.x < maxSouth && f.fields[rock.x+1][rock.y] == empty {
			f.fields[rock.x][rock.y] = empty
			rock.x++
			f.fields[rock.x][rock.y] = round
			moved = true
		}
	}
	return moved
}

func (f *Field) moveWest() bool {
	moved := false
	for _, rock := range f.rocks {
		if rock.y > 0 && f.fields[rock.x][rock.y-1] == empty {
			f.fields[rock.x][rock.y] = empty
			rock.y--
			f.fields[rock.x][rock.y] = round
			moved = true
		}
	}
	return moved
}

func (f *Field) moveEast() bool {
	moved := false
	maxEast := len(f.fields[0]) - 1
	for _, rock := range f.rocks {
		if rock.y < maxEast && f.fields[rock.x][rock.y+1] == empty {
			f.fields[rock.x][rock.y] = empty
			rock.y++
			f.fields[rock.x][rock.y] = round
			moved = true
		}
	}
	return moved
}

func (f *Field) calculateLoad() int {
	result := 0
	for _, rock := range f.rocks {
		result += len(f.fields) - rock.x
	}
	return result
}

func parseFile(filename string) *Field {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	result := [][]byte{}
	rocks := []*Rock{}
	for x, line := range strings.Split(string(b), "\n") {
		row := make([]byte, len(line))
		for y, item := range line {
			switch item {
			case 'O':
				row[y] = round
				rocks = append(rocks, &Rock{x: x, y: y})
			case '#':
				row[y] = blocky
			}
		}
		result = append(result, row)
	}
	return &Field{
		fields: result,
		rocks:  rocks,
	}
}

func (f *Field) String() string {
	b := strings.Builder{}
	for _, row := range f.fields {
		for _, e := range row {
			switch e {
			case empty:
				b.WriteRune('.')
			case round:
				b.WriteRune('O')
			case blocky:
				b.WriteRune('#')
			}
		}
		b.WriteRune('\n')
	}
	return b.String()
}
