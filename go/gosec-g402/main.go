package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func main() {
	// G402: InsecureSkipVerify set to true
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: true,
		},
	}
	client := &http.Client{Transport: tr}
	resp, err := client.Get("https://example.com")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	fmt.Println(resp.Status)
}
