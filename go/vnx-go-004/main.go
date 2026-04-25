package main

import (
	"crypto/tls"
	"net/http"
)

// VNX-GO-004: TLS InsecureSkipVerify enabled
func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	_, _ = client.Get("https://api.example.com/data")
}
