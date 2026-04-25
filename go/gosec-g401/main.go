package main

import (
	"crypto/md5"
	"crypto/sha1"
	"fmt"
)

func main() {
	// G401: Weak hashing algorithm
	h := md5.New()
	fmt.Println(h)

	h2 := sha1.New()
	fmt.Println(h2)
}
