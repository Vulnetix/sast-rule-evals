package main

import (
	"fmt"
	"math"
)

func main() {
	var x int = math.MaxInt
	y := int32(x)  // G115: integer overflow conversion int -> int32
	z := int16(x)  // G115: integer overflow conversion int -> int16
	fmt.Println(y, z)
}
