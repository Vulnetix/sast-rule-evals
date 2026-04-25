package main

import (
	"fmt"
	"os"
)

func main() {
	// G104: Errors unhandled — error return value discarded
	f, _ := os.Open("/etc/passwd")
	fmt.Println(f)
}
