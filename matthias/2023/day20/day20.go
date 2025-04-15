package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strings"
	"time"
)

var (
	reLine = regexp.MustCompile(`(%|&|)(\w+) -> (.+)`)
)

type Signal byte

const (
	Low Signal = iota
	High
)

type Module interface {
	GetName() string
	GetDests() []Module
	Send(source string, signal Signal) []*Event
}

type FlipFlop struct {
	name         string
	destinations []Module
	state        bool
}

type Inverter struct {
	name         string
	destinations []Module
	sourceNames  []string
	lastInputs   map[string]Signal
}

type Broadcaster struct {
	name         string
	destinations []Module
}

type Event struct {
	receiver Module
	signal   Signal
	source   string
}

func main() {
	bc, _ := parseFile("day20/day20.dat")

	t := time.Now()
	var low, high uint64
	for _ = range 1000 {
		l, h := processCycle(bc)
		low += l
		high += h
	}
	fmt.Println("Result 1:", low*high, time.Since(t))

	t = time.Now()
	_, modules := parseFile("day20/day20.dat")
	writesToRx := []Module{}
	for _, m := range modules {
		for _, dest := range m.GetDests() {
			if dest.GetName() == "rx" {
				writesToRx = append(writesToRx, m)
			}
		}
	}
	if len(writesToRx) != 1 {
		panic(fmt.Sprintf("expected only one module to write to rx, but found %d: %v", len(writesToRx), writesToRx))
	}
	actualWriters := []Module{}
	for _, m := range modules {
		if slices.Contains(writesToRx[0].(*Inverter).sourceNames, m.GetName()) {
			actualWriters = append(actualWriters, m)
		}
	}
	if len(actualWriters) != 4 {
		panic(fmt.Sprintf("expected exactly 4 modules to write to rx, but found %d: %v", len(actualWriters), actualWriters))
	}

	result := uint64(1)
	for _, w := range actualWriters {
		bc, _ := parseFile("day20/day20.dat")
		result = lcm(result, processUntilModule(bc, w))
	}
	fmt.Println("Result 2:", result, time.Since(t))
}

func processCycle(bc Module) (low uint64, high uint64) {
	queue := []*Event{{
		receiver: bc,
		signal:   Low,
		source:   "button",
	}}

	for len(queue) > 0 {
		event := queue[0]
		if event.signal == Low {
			low += 1
		} else {
			high += 1
		}

		queue = append(queue[1:], event.receiver.Send(event.source, event.signal)...)
	}
	return low, high
}

func processUntilModule(bc, target Module) (result uint64) {
	result += 1
	for !pressButtonForModule(bc, target) {
		result += 1
	}
	return result
}

func pressButtonForModule(bc, target Module) (result bool) {
	queue := []*Event{{
		receiver: bc,
		signal:   Low,
		source:   "button",
	}}
	targetName := target.GetName()

	for len(queue) > 0 {
		event := queue[0]
		if event.receiver.GetName() == targetName && event.signal == Low {
			return true
		}

		queue = append(queue[1:], event.receiver.Send(event.source, event.signal)...)
	}

	return result
}

func parseFile(filename string) (Module, []Module) {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	assignments := map[string][]string{}
	byName := map[string]Module{}
	modules := []Module{}
	for _, row := range strings.Split(string(b), "\n") {
		parts := reLine.FindStringSubmatch(row)
		if len(parts) != 4 {
			panic(fmt.Sprintf("expected %q to parse into 4 parts but where %v", row, parts))
		}

		name := parts[2]
		assignments[name] = strings.Split(parts[3], ", ")
		var module Module
		switch parts[1] {
		case "":
			module = &Broadcaster{name: name}
		case "%":
			module = &FlipFlop{name: name}
		case "&":
			module = &Inverter{name: name, lastInputs: make(map[string]Signal)}
		default:
			panic(fmt.Sprintf("type %q not found", parts[1]))
		}
		byName[name] = module
		modules = append(modules, module)
	}
	for _, module := range modules {
		for _, name := range assignments[module.GetName()] {
			dest, ok := byName[name]
			if !ok {
				dest = &Broadcaster{name: name}
				byName[name] = dest
			}

			switch module := module.(type) {
			case *Broadcaster:
				module.destinations = append(module.destinations, dest)
			case *FlipFlop:
				module.destinations = append(module.destinations, dest)
			case *Inverter:
				module.destinations = append(module.destinations, dest)
			}
			if destInv, ok := dest.(*Inverter); ok {
				destInv.sourceNames = append(destInv.sourceNames, module.GetName())
			}
		}
	}
	return byName["broadcaster"], modules
}

func (ff *FlipFlop) GetName() string {
	return ff.name
}

func (ff *FlipFlop) GetDests() []Module {
	return ff.destinations
}

func (ff *FlipFlop) Send(_ string, signal Signal) (result []*Event) {
	if signal == High {
		return
	}
	ff.state = !ff.state
	var output = Low
	if ff.state {
		output = High
	}
	for _, mod := range ff.destinations {
		result = append(result, &Event{
			receiver: mod,
			signal:   output,
			source:   ff.name,
		})
	}
	return result
}

func (inv *Inverter) GetName() string {
	return inv.name
}

func (inv *Inverter) GetDests() []Module {
	return inv.destinations
}

func (inv *Inverter) Send(source string, signal Signal) (result []*Event) {
	var output Signal = Low
	inv.lastInputs[source] = signal
	for _, s := range inv.sourceNames {
		if inv.lastInputs[s] == Low {
			output = High
		}
	}

	if signal == Low {
		output = High
	}
	for _, mod := range inv.destinations {
		result = append(result, &Event{
			receiver: mod,
			signal:   output,
			source:   inv.name,
		})
	}
	return result
}

func (inv Inverter) String() string {
	return "&" + inv.name
}

func (bc *Broadcaster) GetName() string {
	return bc.name
}

func (bc *Broadcaster) GetDests() []Module {
	return bc.destinations
}

func (bc *Broadcaster) Send(_ string, signal Signal) (result []*Event) {
	for _, mod := range bc.destinations {
		result = append(result, &Event{
			receiver: mod,
			signal:   signal,
			source:   bc.name,
		})
	}
	return result
}

func gcd(a, b uint64) uint64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b uint64) uint64 {
	return (a * b) / gcd(a, b)
}
