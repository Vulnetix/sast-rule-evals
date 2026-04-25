package main

import (
	"database/sql"
	"fmt"
)

// VNX-GO-003: SQL injection via fmt.Sprintf
func getUser(db *sql.DB, name string) {
	row := db.QueryRow(fmt.Sprintf("SELECT * FROM users WHERE name = '%s'", name))
	_ = row
}
