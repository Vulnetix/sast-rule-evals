package main

import (
	"fmt"
	"net"
)

func main() {
	// G102: Bind to all interfaces
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		panic(err)
	}
	fmt.Println("listening on", ln.Addr())
}
