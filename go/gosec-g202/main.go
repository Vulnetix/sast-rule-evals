package main

import (
	"database/sql"
	"fmt"
	"net/http"
)

var db *sql.DB

func handler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")
	// G202: SQL query built with string concatenation
	query := "SELECT * FROM users WHERE name='" + name + "'"
	rows, err := db.Query(query)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	defer rows.Close()
	fmt.Fprintf(w, "ok")
}

func main() {
	http.HandleFunc("/user", handler)
	http.ListenAndServe(":8080", nil)
}
