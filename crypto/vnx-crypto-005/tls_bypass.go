package main

import (
	"crypto/tls"
	"net/http"
)

// VNX-CRYPTO-005: TLS certificate validation disabled
func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	client.Get("https://api.example.com/data")
}
