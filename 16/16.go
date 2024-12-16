package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	globalStart, globalEnd [2]int
	inp                    [][]rune
)

func main() {
	// Read input from file
	file, err := os.Open("in")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		inp = append(inp, []rune(line))
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Find global start and end positions
	for i := range inp {
		for j := range inp[i] {
			if inp[i][j] == 'S' {
				globalStart = [2]int{i, j}
			}
			if inp[i][j] == 'E' {
				globalEnd = [2]int{i, j}
			}
		}
	}

	test()
}

func test() {
	allPaths := [][][][2]int{}
	pathStack := [][][][2]int{{{globalStart, {1}}}}

	bfs := func() {
		ii := 0
		for len(pathStack) > 0 {
			if ii%10000 == 0 {
				fmt.Println(len(pathStack))
			}
			ii++
			path := pathStack[0]
			pathStack = pathStack[1:]
			x, y := path[len(path)-1][0][0], path[len(path)-1][0][1]
			dir := path[len(path)-1][1][0]
			if x == globalEnd[0] && y == globalEnd[1] {
				allPaths = append(allPaths, path)
			}
			for _, d := range [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
				newX, newY := x+d[0], y+d[1]
				if newX >= 0 && newX < len(inp) && newY >= 0 && newY < len(inp[0]) && inp[newX][newY] != '#' {
					visited := false
					for _, p := range path {
						if p[0][0] == newX && p[0][1] == newY {
							visited = true
							break
						}
					}
					if !visited {
						newDir := dir
						switch {
						case d[0] == 1 && d[1] == 0:
							newDir = 2
						case d[0] == -1 && d[1] == 0:
							newDir = 0
						case d[0] == 0 && d[1] == 1:
							newDir = 1
						case d[0] == 0 && d[1] == -1:
							newDir = 3
						}
						newPath := append(path, [][2]int{{newX, newY}, {newDir, 0}})
						pathStack = append(pathStack, newPath)
					}
				}
			}
		}
	}

	bfs()

	pathScores := []int{}
	for _, path := range allPaths {
		score := len(path) - 1
		for i := 1; i < len(path); i++ {
			if path[i][1] != path[i-1][1] {
				score++
			}
		}
		pathScores = append(pathScores, score)
	}

	minScore := pathScores[0]
	for _, score := range pathScores {
		if score < minScore {
			minScore = score
		}
	}

	fmt.Println(minScore)
}
