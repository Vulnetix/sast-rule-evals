package main

import (
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	path := r.FormValue("file")
	data, err := os.ReadFile(path) // G703/G304: path traversal
	if err != nil {
		http.Error(w, "not found", 404)
		return
	}
	fmt.Fprintln(w, string(data))
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
