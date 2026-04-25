package main

import (
	"net/http"
	"text/template"
)

func handler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")
	tmpl := "Hello, " + name + "!" // G708: server-side template injection via string concat
	t, _ := template.New("").Parse(tmpl)
	t.Execute(w, nil) //nolint
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
