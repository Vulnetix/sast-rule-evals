package main

import (
	"fmt"

	"golang.org/x/crypto/md4" // G406/G506: use of weak cryptographic primitive MD4
)

func main() {
	h := md4.New()
	h.Write([]byte("data"))
	fmt.Printf("%x\n", h.Sum(nil))
}
