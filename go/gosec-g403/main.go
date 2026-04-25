package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

func main() {
	// G403: RSA key too small (1024 bits)
	key, err := rsa.GenerateKey(rand.Reader, 1024)
	if err != nil {
		panic(err)
	}
	fmt.Println(key.Size())
}
