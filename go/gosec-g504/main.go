package main

import (
	"fmt"
	"net/http/cgi"
)

func main() {
	// G504: Import of net/http/cgi — HTTPoxy vulnerability
	handler := cgi.Handler{
		Path: "/usr/lib/cgi-bin/app",
	}
	fmt.Println(handler)
}
