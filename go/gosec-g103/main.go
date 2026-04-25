package main

import (
	"fmt"
	"unsafe"
)

func main() {
	// G103: Use of unsafe block
	x := 42
	ptr := unsafe.Pointer(&x)
	fmt.Println(ptr)
}
