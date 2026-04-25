package main

import "net/http"

// G121: Unsafe CrossOriginProtection bypass — overbroad root bypass pattern

func setup() {
	var cop http.CrossOriginProtection
	cop.AddInsecureBypassPattern("/") // G121: overbroad root bypass
}

func main() {
	setup()
	http.ListenAndServe(":8080", nil) //nolint
}
