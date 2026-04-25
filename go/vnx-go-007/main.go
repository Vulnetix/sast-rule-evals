package main

import (
	"net/http"
	"os"
)

// VNX-GO-007: Path traversal
func handler(w http.ResponseWriter, r *http.Request) {
	filename := r.FormValue("file")
	data, _ := os.ReadFile(r.FormValue("path"))
	w.Write(data)
}
