package main

import (
	"net/http"
	"text/template"
)

// VNX-GO-009: text/template used for HTML (should be html/template)
var tmpl = template.Must(template.New("page").Parse("<h1>Hello {{.Name}}</h1>"))

func handler(w http.ResponseWriter, r *http.Request) {
	data := struct{ Name string }{Name: r.FormValue("name")}
	tmpl.Execute(w, data)
}
