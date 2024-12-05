package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

var (
	nodePattern = regexp.MustCompile(`(\w+) = \((\w+), (\w+)\)`)
)

const (
	start = "AAA"
	end   = "ZZZ"
	left  = byte(76) // L
	right = byte(82) // R
	nodeA = byte(65) // A
	nodeZ = byte(90) // Z
)

type Node struct {
	Name  string
	Left  string
	Right string
}

func (n *Node) String() string {
	return n.Name + " = (" + n.Left + ", " + n.Right + ")"
}

type NodeMap struct {
	Nodes map[string]*Node
	Path  string
}

func (nm *NodeMap) String() string {
	result := nm.Path + "\n"
	for _, n := range nm.Nodes {
		result += "\n" + n.String()
	}
	return result
}

func main() {
	nodeMap := parseFile("day08/day08.dat")

	node := start
	pos := 0
	steps := int64(0)
	for node != end {
		if nodeMap.Path[pos] == left {
			node = nodeMap.Nodes[node].Left
		} else {
			node = nodeMap.Nodes[node].Right
		}
		pos = (pos + 1) % len(nodeMap.Path)
		steps++
	}
	fmt.Println("Result 1:", steps)

	// nodeMap = parseFile("day08/example3.dat")
	nodes := nodeMap.findStartingNodes()
	pos = 0
	steps = 0
	// endNodes := nodeMap.indexEndNodes()
	for !allDone(nodes) {
		if nodeMap.Path[pos] == left {
			for i, n := range nodes {
				nodes[i] = nodeMap.Nodes[n].Left
			}
		} else {
			for i, n := range nodes {
				nodes[i] = nodeMap.Nodes[n].Right
			}
		}
		pos = (pos + 1) % len(nodeMap.Path)
		steps++
		if steps%10000000 == 0 {
			fmt.Println(steps, howManyDone(nodes), "/", len(nodes))
		}
	}
	fmt.Println("Result 2:", steps)
}

func parseFile(filename string) *NodeMap {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	parts := strings.Split(string(b), "\n\n")
	result := &NodeMap{
		Path:  parts[0],
		Nodes: make(map[string]*Node),
	}
	for _, line := range strings.Split(parts[1], "\n") {
		matches := nodePattern.FindAllStringSubmatch(line, 10000)
		result.Nodes[matches[0][1]] = &Node{
			Name:  matches[0][1],
			Left:  matches[0][2],
			Right: matches[0][3],
		}
	}
	return result
}

func (nm *NodeMap) findStartingNodes() []string {
	result := []string{}
	for node, _ := range nm.Nodes {
		if node[len(node)-1] == nodeA {
			result = append(result, node)
		}
	}
	return result
}

func allDone(nodes []string) bool {
	for _, n := range nodes {
		if n[len(n)-1] != nodeZ {
			return false
		}
	}
	return true
}

func howManyDone(nodes []string) int {
	result := 0
	for _, n := range nodes {
		if n[len(n)-1] == nodeZ {
			result++
		}
	}
	return result
}
