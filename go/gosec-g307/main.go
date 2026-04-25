package main

import (
	"fmt"
	"os"
)

func main() {
	// G307: os.Create uses default permissions (0666) which may be too permissive
	// NOTE: requires -conf config.json with {"G307": "0600"} to trigger
	f, err := os.Create("output.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	fmt.Fprintln(f, "data")
}
