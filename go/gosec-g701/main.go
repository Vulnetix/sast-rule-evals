package main

import (
	"database/sql"
	"fmt"
	"net/http"
)

var db *sql.DB

func handler(w http.ResponseWriter, r *http.Request) {
	// G701: SQL injection taint — user input flows into db.Query
	id := r.URL.Query().Get("id")
	rows, err := db.Query("SELECT * FROM users WHERE id=" + id)
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
