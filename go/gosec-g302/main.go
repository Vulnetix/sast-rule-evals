package main

import "os"

func main() {
	// G302: File created with excessive permissions
	f, err := os.OpenFile("/tmp/config.txt", os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		panic(err)
	}
	defer f.Close()
}
