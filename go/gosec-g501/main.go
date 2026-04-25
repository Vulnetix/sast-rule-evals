package main

import (
	"crypto/md5"
	"fmt"
)

func hash(data string) []byte {
	// G501: Import of crypto/md5
	h := md5.Sum([]byte(data))
	return h[:]
}

func main() {
	fmt.Printf("%x\n", hash("hello"))
}
