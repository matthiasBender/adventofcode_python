package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

var (
	rePart      = regexp.MustCompile(`x=(\d+),m=(\d+),a=(\d+),s=(\d+)`)
	reRule      = regexp.MustCompile(`(\w+)\{(.+)\}`)
	reCondition = regexp.MustCompile(`(\w)(<|>)(\d+):(\w+)`)
	fullRange   = &PartRange{
		x: &Range{start: 1, end: 4000},
		m: &Range{start: 1, end: 4000},
		a: &Range{start: 1, end: 4000},
		s: &Range{start: 1, end: 4000},
	}
)

type Comp byte

const (
	maxN  uint64 = 4000
	empty Comp   = iota
	greaterThan
	lessThan
)

type Range struct {
	start, end uint64
}

type PartRange struct {
	x, m, a, s *Range
}

type Part struct {
	x, m, a, s uint64
}

type Condition struct {
	name       string
	targetRule string
	applies    func(*Part) bool
	barrier    uint64
	comp       Comp
	attr       string
}

type Rule struct {
	name       string
	conditions []*Condition
}

type RuleWithRange struct {
	rule   string
	prange *PartRange
}

func main() {
	parts, rules := parseFile("day19/day19.dat")
	accepted := []*Part{}
	rejected := []*Part{}
	rules["A"] = generateCaptureRule("A", &accepted)
	rules["R"] = generateCaptureRule("R", &rejected)

	t := time.Now()
	for _, p := range parts {
		ruleName := "in"
		for ruleName != "" {
			rule := rules[ruleName]
			ruleName = ""
			for _, condition := range rule.conditions {
				if condition.applies(p) {
					ruleName = condition.targetRule
					break
				}
			}
		}
	}
	fmt.Println("Result 1:", sum(accepted), time.Since(t))

	t = time.Now()
	fmt.Println("Result 2:", scoreRanges(determineAcceptedRanges(rules)), time.Since(t))
}

func sum(parts []*Part) (result uint64) {
	for _, p := range parts {
		result += p.x + p.m + p.a + p.s
	}
	return result
}

func scoreRanges(ranges []*PartRange) (result uint64) {
	for _, rng := range ranges {
		result += (rng.x.end - rng.x.start + 1) * (rng.m.end - rng.m.start + 1) * (rng.a.end - rng.a.start + 1) * (rng.s.end - rng.s.start + 1)
	}
	return result
}

func determineAcceptedRanges(rules map[string]*Rule) (result []*PartRange) {
	ruleRanges := []*RuleWithRange{{rule: "in", prange: fullRange}}
	for len(ruleRanges) > 0 {
		rr := ruleRanges[0]
		ruleRanges = ruleRanges[1:]
		if rr.rule == "A" {
			result = append(result, rr.prange)
			continue
		}
		if rr.rule == "R" {
			continue
		}
		rule := rules[rr.rule]
		rng := rr.prange
		for _, c := range rule.conditions {
			lower, upper := rng.toParts()
			contLow := c.applies(lower)
			contUp := c.applies(upper)
			if contLow && contUp {
				ruleRanges = append(ruleRanges, &RuleWithRange{rule: c.targetRule, prange: rng})
				break
			}
			if !contLow && !contUp {
				continue
			}
			var rngNew *PartRange
			rngNew, rng = splitRanges(rng, c)
			ruleRanges = append(ruleRanges, &RuleWithRange{rule: c.targetRule, prange: rngNew})
		}
	}

	return result
}

func splitRanges(rng *PartRange, condition *Condition) (*PartRange, *PartRange) {
	rngNew := rng.Copy()
	var rNew, rOld *Range
	switch condition.attr {
	case "x":
		rNew = rngNew.x
		rOld = rng.x
	case "m":
		rNew = rngNew.m
		rOld = rng.m
	case "a":
		rNew = rngNew.a
		rOld = rng.a
	case "s":
		rNew = rngNew.s
		rOld = rng.s
	}

	if condition.comp == greaterThan {
		rOld.end = condition.barrier
		rNew.start = condition.barrier + 1
	}
	if condition.comp == lessThan {
		rOld.start = condition.barrier
		rNew.end = condition.barrier - 1
	}
	return rngNew, rng
}

func parseFile(filename string) (parts []*Part, rules map[string]*Rule) {
	b, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	rules = make(map[string]*Rule)
	blocks := strings.Split(string(b), "\n\n")
	for _, row := range strings.Split(blocks[0], "\n") {
		heads := reRule.FindStringSubmatch(row)
		name := heads[1]
		conditions := []*Condition{}
		for _, condStr := range strings.Split(heads[2], ",") {
			if !reCondition.MatchString(condStr) {
				conditions = append(conditions, &Condition{
					targetRule: condStr,
					applies:    func(_ *Part) bool { return true },
				})
				continue
			}
			condParts := reCondition.FindStringSubmatch(condStr)
			comp := generateComp(condParts[2])
			numb := generateBarrier(condParts[3])
			conditions = append(conditions, &Condition{
				name:       condParts[1] + condParts[2] + condParts[3],
				targetRule: condParts[4],
				applies:    generateRuleFunc(condParts[1], comp, numb),
				barrier:    numb,
				comp:       comp,
				attr:       condParts[1],
			})
		}

		rules[name] = &Rule{
			name:       name,
			conditions: conditions,
		}
	}
	for _, row := range strings.Split(blocks[1], "\n") {
		partNums := rePart.FindStringSubmatch(row)
		x, _ := strconv.ParseUint(partNums[1], 10, 64)
		m, _ := strconv.ParseUint(partNums[2], 10, 64)
		a, _ := strconv.ParseUint(partNums[3], 10, 64)
		s, _ := strconv.ParseUint(partNums[4], 10, 64)
		parts = append(parts, &Part{
			x: x, m: m,
			a: a, s: s,
		})
	}
	return parts, rules
}

func generateRuleFunc(attr string, comp Comp, numb uint64) func(*Part) bool {
	var selector func(*Part) uint64
	switch attr {
	case "x":
		selector = GetX
	case "m":
		selector = GetM
	case "a":
		selector = GetA
	case "s":
		selector = GetS
	default:
		panic(fmt.Errorf("found %q for attr", attr))
	}

	if comp == lessThan {
		return func(p *Part) bool {
			return selector(p) < numb
		}
	}

	return func(p *Part) bool {
		return selector(p) > numb
	}
}

func generateComp(comp string) Comp {
	if comp == "<" {
		return lessThan
	}
	return greaterThan
}

func generateBarrier(numb string) uint64 {
	n, err := strconv.ParseUint(numb, 10, 64)
	if err != nil {
		panic(err)
	}
	return n
}

func generateCaptureRule(name string, collector *[]*Part) *Rule {
	return &Rule{
		name: name,
		conditions: []*Condition{{
			applies: func(p *Part) bool {
				*collector = append(*collector, p)
				return false
			},
		}},
	}
}

func GetX(p *Part) uint64 {
	return p.x
}
func GetM(p *Part) uint64 {
	return p.m
}
func GetA(p *Part) uint64 {
	return p.a
}
func GetS(p *Part) uint64 {
	return p.s
}

func (p Part) String() string {
	return fmt.Sprintf("{x=%d, m=%d, a=%d, s=%d}", p.x, p.m, p.a, p.s)
}

func (c Condition) String() string {
	return c.name + ":" + c.targetRule
}

func (r Rule) String() string {
	condStrings := make([]string, 0, len(r.conditions))
	for _, c := range r.conditions {
		condStrings = append(condStrings, c.String())
	}
	return fmt.Sprintf("%s{%s}", r.name, strings.Join(condStrings, ","))
}

func (pr PartRange) String() string {
	return fmt.Sprintf(
		"{x: [%d, %d], m: [%d, %d], a: [%d, %d], s: [%d, %d]}",
		pr.x.start, pr.x.end,
		pr.m.start, pr.m.end,
		pr.a.start, pr.a.end,
		pr.s.start, pr.s.end,
	)
}

func (pr *PartRange) Copy() *PartRange {
	return &PartRange{
		x: &Range{start: pr.x.start, end: pr.x.end},
		m: &Range{start: pr.m.start, end: pr.m.end},
		a: &Range{start: pr.a.start, end: pr.a.end},
		s: &Range{start: pr.s.start, end: pr.s.end},
	}
}

func (pr *PartRange) toParts() (*Part, *Part) {
	return &Part{
			x: pr.x.start,
			m: pr.m.start,
			a: pr.a.start,
			s: pr.s.start,
		}, &Part{
			x: pr.x.end,
			m: pr.m.end,
			a: pr.a.end,
			s: pr.s.end,
		}
}
