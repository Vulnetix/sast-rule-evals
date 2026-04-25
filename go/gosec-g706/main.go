package main

import (
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	user := r.FormValue("user")
	log.Printf("User logged in: %s", user) // G706: log injection via tainted input
	w.Write([]byte("ok"))                  //nolint
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
