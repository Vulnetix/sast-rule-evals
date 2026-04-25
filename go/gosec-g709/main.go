package main

import (
	"encoding/gob"
	"net/http"
	"strings"
)

type User struct {
	Name string
	Role string
}

func handler(w http.ResponseWriter, r *http.Request) {
	data := r.FormValue("data")
	dec := gob.NewDecoder(strings.NewReader(data))
	var user User
	dec.Decode(&user) // G709: unsafe deserialization of tainted user input
	_ = user
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
