package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	userInput := os.Args[1]
	// VNX-GO-002: exec.Command with fmt.Sprintf
	cmd := exec.Command("sh", "-c", fmt.Sprintf("echo %s", userInput))
	cmd.Run()
}
