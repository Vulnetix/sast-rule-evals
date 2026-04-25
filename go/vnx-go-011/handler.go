// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-011: Go gob deserialization from HTTP request body

package main

import (
	"encoding/gob"
	"net/http"
)

type UserData struct {
	ID    int
	Name  string
	Email string
}

func handleDecode(w http.ResponseWriter, r *http.Request) {
	var userData UserData
	// VULNERABLE: gob.NewDecoder directly from HTTP request body without size limits
	err := gob.NewDecoder(r.Body).Decode(&userData)
	if err != nil {
		http.Error(w, "Decode error", http.StatusBadRequest)
		return
	}
	// Process userData...
}
