package main

import (
	"net/http"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	http.SetCookie(w, &http.Cookie{ // G124: missing Secure and HttpOnly flags
		Name:    "session",
		Value:   "abc123",
		Expires: time.Now().Add(24 * time.Hour),
	})
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
