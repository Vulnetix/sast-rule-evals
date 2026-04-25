package main

import (
	"fmt"
	"net/http"
	"os/exec"
)

func handler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("cmd")
	// G204: Command injection via exec.Command with user input
	out, err := exec.Command("echo", name).Output()
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	fmt.Fprintf(w, string(out))
}

func main() {
	http.HandleFunc("/run", handler)
	http.ListenAndServe(":8080", nil)
}
