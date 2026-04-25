package main

import (
	"crypto/aes"
	"crypto/cipher"
	"fmt"
)

func main() {
	key := make([]byte, 32)
	block, _ := aes.NewCipher(key)
	iv := []byte{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0} // G407: hardcoded IV/nonce
	stream := cipher.NewCFBEncrypter(block, iv)
	src := []byte("plaintext here!!")
	dst := make([]byte, len(src))
	stream.XORKeyStream(dst, src)
	fmt.Printf("%x\n", dst)
}
