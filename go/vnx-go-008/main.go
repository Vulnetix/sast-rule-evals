package main

import (
	"fmt"
	"math/rand"
)

// VNX-GO-008: Weak PRNG
func generateToken() string {
	const chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	token := make([]byte, 32)
	for i := range token {
		token[i] = chars[rand.Intn(len(chars))]
	}
	return string(token)
}

func main() {
	fmt.Println(generateToken())
}
