package main

import "os"

func main() {
	// G104: Errors unhandled — error return value not captured at all
	os.Remove("/tmp/test")
	os.Mkdir("/tmp/testdir", 0755)
}
