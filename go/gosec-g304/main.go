package main

import (
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	filename := r.FormValue("file")
	// G304: File path from user input — path traversal risk
	data, err := os.ReadFile(filename)
	if err != nil {
		http.Error(w, err.Error(), 404)
		return
	}
	fmt.Fprintf(w, string(data))
}

func main() {
	http.HandleFunc("/read", handler)
	http.ListenAndServe(":8080", nil)
}
