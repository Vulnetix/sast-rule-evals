package main

import "net/http"

func main() {
	// G111: File server serving from root directory
	http.Handle("/files/", http.FileServer(http.Dir("/")))
	http.ListenAndServe(":8080", nil)
}
