package main

import (
	"crypto/des"
	"fmt"
)

func main() {
	// G502: Import of crypto/des
	key := []byte("8bytekey")
	c, err := des.NewCipher(key)
	if err != nil {
		panic(err)
	}
	fmt.Println(c.BlockSize())
}
