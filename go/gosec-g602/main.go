package main

import "fmt"

func main() {
	s := make([]byte, 0)
	fmt.Println(s[:3]) // G602: slice bounds out of range — s has len 0, accessing up to index 3
}
