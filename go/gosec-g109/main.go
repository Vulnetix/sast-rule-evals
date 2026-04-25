package main

import (
	"fmt"
	"strconv"
)

func main() {
	// G109: strconv.Atoi converted to int32 — potential overflow
	n, err := strconv.Atoi("12345")
	if err != nil {
		panic(err)
	}
	val := int32(n) // G109: overflow possible
	fmt.Println(val)
}
