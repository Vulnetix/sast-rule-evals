package main

import (
	"fmt"
	"net/http"
	"os/exec"
)

func handler(w http.ResponseWriter, r *http.Request) {
	cmd := r.FormValue("cmd")
	out, _ := exec.Command("sh", "-c", cmd).Output() // G702/G204: command injection
	fmt.Fprintln(w, string(out))
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
