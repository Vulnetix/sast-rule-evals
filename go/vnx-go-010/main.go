package main

import (
	"crypto/des"
	"fmt"
)

// VNX-GO-010: Weak cipher (DES)
func main() {
	key := []byte("12345678")
	block, _ := des.NewCipher(key)
	fmt.Println(block)
}
