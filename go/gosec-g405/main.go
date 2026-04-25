package main

import (
	"crypto/des"
	"fmt"
)

func main() {
	// G405: Weak cipher — DES
	key := []byte("8bytekey")
	c, err := des.NewCipher(key)
	if err != nil {
		panic(err)
	}
	fmt.Println("block size:", c.BlockSize())
}
