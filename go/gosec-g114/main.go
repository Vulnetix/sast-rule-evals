package main

import "net/http"

func main() {
	// G114: http.ListenAndServe without timeout configuration
	http.ListenAndServe(":8080", nil)
}
