package main

import (
	"advent-of-code/go/utils"
	"container/heap"
	"fmt"
	"os"
	"regexp"
)

func main() {
	env := os.Getenv("AOC_ENV")
	input, err := utils.ReadFile(env, "2024", "1")
	if err != nil {
		panic(err)
	}

	// Part 1
	part1Result := solvePart1(input)
	fmt.Printf("Part 1: %d\n", part1Result)

	// Part 2
	part2Result := solvePart2(input)
	fmt.Printf("Part 2: %d\n", part2Result)
}

func solvePart1(lines []byte) int {
	leftHeap := &utils.IntHeap{}
	rightHeap := &utils.IntHeap{}
	r, _ := regexp.Compile(`(\d+)\s+(\d+)`)

	op := r.FindAllSubmatch(lines, -1)
	heap.Init(leftHeap)
	heap.Init(rightHeap)

	for _, a := range op {
		left, _ := utils.ByteToInt(a[1])
		right, _ := utils.ByteToInt(a[2])
		heap.Push(leftHeap, left)
		heap.Push(rightHeap, right)
	}

	dist := 0
	for leftHeap.Len() > 0 {
		left := heap.Pop(leftHeap).(int)
		right := heap.Pop(rightHeap).(int)
		if left < right {
			dist += right - left
		} else {
			dist += left - right
		}
	}

	return dist
}

func solvePart2(lines []byte) int {
	leftElements := []int{}
	rightMap := make(map[int]int)
	r, _ := regexp.Compile(`(\d+)\s+(\d+)`)

	op := r.FindAllSubmatch(lines, -1)

	for _, a := range op {
		left, _ := utils.ByteToInt(a[1])
		right, _ := utils.ByteToInt(a[2])
		leftElements = append(leftElements, left)
		rightMap[right]++
	}

	similarityScore := 0
	for _, left := range leftElements {
		similarityScore += left * rightMap[left]
	}
	return similarityScore
}
