package main

import "os"

func main() {
	// G306: File write with world-readable permissions
	os.WriteFile("/tmp/config.json", []byte(`{"key":"value"}`), 0644)
}
