package main

import (
	"fmt"
	"net/http"
)

func upload(w http.ResponseWriter, r *http.Request) {
	r.ParseMultipartForm(0) // G120: no size limit
	fmt.Fprintln(w, "ok")
}

func main() {
	http.HandleFunc("/upload", upload)
	http.ListenAndServe(":8080", nil) //nolint
}
