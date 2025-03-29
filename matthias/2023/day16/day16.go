package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	empty         = byte(0) // '.'
	mirrorBack    = byte(1) // '\'
	mirrorFwd     = byte(2) // '/'
	shardVertical = byte(3) // '|'
	shardHoriz    = byte(4) // '-'
)

type Board struct {
	board [][]byte
}

type Direction int

const (
	Right Direction = iota
	Left
	Up
	Down
)

type Coordinate struct {
	x, y int
}

type Beam struct {
	x, y      int
	direction Direction
}

func main() {
	board := parseFile("day16/day16.dat")
	fmt.Println("Result 1:", energizeBoard(board, &Beam{
		x:         0,
		y:         0,
		direction: Right,
	}))
	fmt.Println("Result 2:", maxEnergized(board))
}

func maxEnergized(board *Board) int {
	result := 0

	for newX := range board.board {
		if e := energizeBoard(board, &Beam{x: newX, y: 0, direction: Right}); e > result {
			result = e
		}
		if e := energizeBoard(board, &Beam{x: newX, y: len(board.board[0]) - 1, direction: Left}); e > result {
			result = e
		}
	}
	for newY := range board.board[0] {
		if e := energizeBoard(board, &Beam{x: 0, y: newY, direction: Down}); e > result {
			result = e
		}
		if e := energizeBoard(board, &Beam{x: len(board.board) - 1, y: newY, direction: Up}); e > result {
			result = e
		}
	}

	return result
}

func energizeBoard(board *Board, start *Beam) int {
	queue := NewQ[Beam]()
	queue.Push(*start)
	for !queue.Empty() {
		for _, b := range board.generateNextBeams(queue.Pop()) {
			queue.Push(*b)
		}
	}
	return energizedFields(queue)
}

func energizedFields(q *MemQueue[Beam]) (result int) {
	found := map[Coordinate]bool{}
	for _, beam := range q.CacheElements() {
		c := &Coordinate{x: beam.x, y: beam.y}
		if !found[*c] {
			found[*c] = true
			result++
		}
	}
	return result
}

func (b *Board) generateNextBeams(beam Beam) (result []*Beam) {
	field := b.board[beam.x][beam.y]
	if b.goesUp(&beam, field) {
		result = append(result, &Beam{x: beam.x - 1, y: beam.y, direction: Up})
	}
	if b.goesDown(&beam, field) {
		result = append(result, &Beam{x: beam.x + 1, y: beam.y, direction: Down})
	}
	if b.goesLeft(&beam, field) {
		result = append(result, &Beam{x: beam.x, y: beam.y - 1, direction: Left})
	}
	if b.goesRight(&beam, field) {
		result = append(result, &Beam{x: beam.x, y: beam.y + 1, direction: Right})
	}
	return result
}

func (b *Board) goesUp(beam *Beam, field byte) bool {
	return beam.x > 0 && ((field == empty && beam.direction == Up) ||
		(field == shardVertical && beam.direction != Down) ||
		(field == mirrorFwd && beam.direction == Right) ||
		(field == mirrorBack && beam.direction == Left))
}

func (b *Board) goesDown(beam *Beam, field byte) bool {
	return beam.x < len(b.board)-1 && ((field == empty && beam.direction == Down) ||
		(field == shardVertical && beam.direction != Up) ||
		(field == mirrorFwd && beam.direction == Left) ||
		(field == mirrorBack && beam.direction == Right))
}

func (b *Board) goesLeft(beam *Beam, field byte) bool {
	return beam.y > 0 && ((field == empty && beam.direction == Left) ||
		(field == shardHoriz && beam.direction != Right) ||
		(field == mirrorFwd && beam.direction == Down) ||
		(field == mirrorBack && beam.direction == Up))
}

func (b *Board) goesRight(beam *Beam, field byte) bool {
	return beam.y < len(b.board[0])-1 && ((field == empty && beam.direction == Right) ||
		(field == shardHoriz && beam.direction != Left) ||
		(field == mirrorFwd && beam.direction == Up) ||
		(field == mirrorBack && beam.direction == Down))
}

func parseFile(filename string) *Board {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	var result [][]byte
	for _, line := range strings.Split(string(b), "\n") {
		row := []byte{}
		for _, c := range line {
			switch c {
			case '.':
				row = append(row, empty)
			case '\\':
				row = append(row, mirrorBack)
			case '/':
				row = append(row, mirrorFwd)
			case '-':
				row = append(row, shardHoriz)
			case '|':
				row = append(row, shardVertical)
			}
		}
		result = append(result, row)
	}
	return &Board{result}
}

func (f *Board) String() string {
	sb := strings.Builder{}
	for _, row := range f.board {
		for _, item := range row {
			switch item {
			case empty:
				sb.WriteRune('.')
			case mirrorBack:
				sb.WriteRune('\\')
			case mirrorFwd:
				sb.WriteRune('/')
			case shardVertical:
				sb.WriteRune('|')
			case shardHoriz:
				sb.WriteRune('-')
			}
		}
		sb.WriteRune('\n')
	}
	return sb.String()
}

func (b Beam) String() string {
	sb := strings.Builder{}
	sb.WriteRune('<')
	sb.WriteString(strconv.Itoa(b.x))
	sb.WriteString(", ")
	sb.WriteString(strconv.Itoa(b.y))
	sb.WriteRune('|')
	switch b.direction {
	case Right:
		sb.WriteString("RIGHT")
	case Left:
		sb.WriteString("LEFT")
	case Up:
		sb.WriteString("UP")
	case Down:
		sb.WriteString("DOWN")
	}
	sb.WriteRune('>')
	return sb.String()
}

func (c Coordinate) String() string {
	return fmt.Sprintf("<%d, %d>", c.x, c.y)
}
