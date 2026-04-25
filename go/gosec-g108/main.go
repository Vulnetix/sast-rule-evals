package main

import (
	"net/http"
	_ "net/http/pprof" // G108: profiling endpoint registered
)

func main() {
	http.ListenAndServe(":6060", nil)
}
