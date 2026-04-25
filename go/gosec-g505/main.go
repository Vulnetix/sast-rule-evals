package main

import (
	"crypto/sha1"
	"fmt"
)

func main() {
	// G505: Import of crypto/sha1
	h := sha1.New()
	h.Write([]byte("hello"))
	fmt.Printf("%x\n", h.Sum(nil))
}
