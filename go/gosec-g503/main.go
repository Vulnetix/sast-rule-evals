package main

import (
	"crypto/rc4"
	"fmt"
)

func main() {
	// G503: Import of crypto/rc4
	key := []byte("somekey")
	c, err := rc4.NewCipher(key)
	if err != nil {
		panic(err)
	}
	msg := []byte("hello world")
	c.XORKeyStream(msg, msg)
	fmt.Printf("%x\n", msg)
}
