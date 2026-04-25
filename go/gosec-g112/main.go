package main

import "net/http"

func main() {
	// Slowloris test: missing timeout on server
	srv := &http.Server{
		Addr: ":8080",
	}
	srv.ListenAndServe()
}
