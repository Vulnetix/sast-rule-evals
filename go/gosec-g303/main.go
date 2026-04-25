package main

import (
	"fmt"
	"os"
)

func main() {
	// G303: Predictable tempfile — empty dir defaults to os.TempDir()
	f, err := os.CreateTemp("", "myapp-*.tmp")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	defer os.Remove(f.Name())
	fmt.Println(f.Name())
}
