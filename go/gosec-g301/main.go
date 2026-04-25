package main

import "os"

func main() {
	// G301: Directory created with excessive permissions
	os.MkdirAll("/tmp/myapp/data", 0755)
}
