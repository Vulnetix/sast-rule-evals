package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

// VNX-CRYPTO-006: Weak RSA key size (1024 bits)
func main() {
	key, _ := rsa.GenerateKey(rand.Reader, 1024)
	fmt.Println(key.PublicKey.N)
}
