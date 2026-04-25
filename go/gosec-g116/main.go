package main

import "fmt"

func main() {
	// The string below contains a bidirectional unicode control character (U+202E)
	msg := "access level: user‮ ⁦// Check if admin⁩ ⁦"
	fmt.Println(msg)
}
