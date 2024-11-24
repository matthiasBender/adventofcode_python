package main

import (
	"fmt"
	"regexp"
	"strconv"
)

const (
	exampleTimes     = "Time:      7  15   30"
	exampleDistances = "Distance:  9  40  200"
	exampleTime2     = int64(71530)
	exampleDist2     = int64(940200)
	inputTimes       = "Time:        38     94     79     70"
	inputDistances   = "Distance:   241   1549   1074   1091"
	inputTime2       = int64(38947970)
	inputDist2       = int64(241154910741091)
)

var (
	numberPattern = regexp.MustCompile(`(\d+)`)
)

func main() {
	times := extractNumbers(inputTimes)
	distances := extractNumbers(inputDistances)

	result1 := 1
	for i, t := range times {
		success := 0
		for hold := int64(0); hold < t; hold++ {
			traveled := findDistance(t, hold)
			if traveled > distances[i] {
				success++
			}
		}
		result1 *= success
	}
	fmt.Println("Result 1:", result1)

	result2 := 0
	t2 := inputTime2
	d2 := inputDist2
	for hold := int64(0); hold < t2; hold++ {
		traveled := findDistance(t2, hold)
		if traveled > d2 {
			result2++
		}
	}
	fmt.Println("Result 2:", result2)
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

func findDistance(maxTime, holdTime int64) int64 {
	return (maxTime - holdTime) * holdTime
}
