package main

import (
	"fmt"
	"net/http"
	"net/smtp"
)

func handler(w http.ResponseWriter, r *http.Request) {
	to := r.FormValue("to")
	subject := r.FormValue("subject")
	msg := []byte("To: " + to + "\r\nSubject: " + subject + "\r\n\r\nHello\r\n")
	err := smtp.SendMail("localhost:25", nil, "from@example.com", []string{to}, msg) // G707: SMTP injection
	if err != nil {
		fmt.Fprintln(w, err)
		return
	}
	fmt.Fprintln(w, "sent")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
