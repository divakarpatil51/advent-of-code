package utils

import (
	"os"
	"path/filepath"
	"strconv"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type FileReadInput struct {
	env  string
	year string
	day  string
}

// ReadFile reads input data for Advent of Code problems
// env: "test" or "real", day: "1", year: "2024"
func ReadFile(env, year, day string) ([]byte, error) {

	cwd, err := os.Getwd()
	if err != nil {
		return nil, err
	}

	filePath := filepath.Join(cwd, "inputs", year, env, day+".txt")

	input, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}

	return input, nil
}

func ByteToInt(b []byte) (int, error) {
	return strconv.Atoi(string(b))
}
