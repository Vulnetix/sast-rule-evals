package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// G705: XSS — user input reflected without escaping
	name := r.FormValue("name")
	w.Header().Set("Content-Type", "text/html")
	fmt.Fprintf(w, "<p>Hello, "+name+"!</p>")
}

func main() {
	http.HandleFunc("/greet", handler)
	http.ListenAndServe(":8080", nil)
}
