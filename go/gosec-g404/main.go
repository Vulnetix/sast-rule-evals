package main

import (
	"fmt"
	"math/rand"
)

func main() {
	// G404: Weak PRNG — math/rand
	token := rand.Intn(1000000)
	fmt.Println("token:", token)
}
