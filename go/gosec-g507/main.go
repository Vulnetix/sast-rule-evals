package main

import (
	"fmt"

	"golang.org/x/crypto/ripemd160" // G507: use of weak cryptographic primitive RIPEMD-160
)

func main() {
	h := ripemd160.New()
	h.Write([]byte("data"))
	fmt.Printf("%x\n", h.Sum(nil))
}
