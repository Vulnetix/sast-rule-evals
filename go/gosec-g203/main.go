package main

import (
	"html/template"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")
	// G203: Unescaped data in HTML template via template.HTML
	tmpl := template.Must(template.New("t").Parse(`<p>Hello {{.}}</p>`))
	tmpl.Execute(w, template.HTML(name))
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
