package main

import "net/http"

// G119: Unsafe redirect policy — copies all headers from previous request, leaking sensitive headers

func client() *http.Client {
	return &http.Client{
		CheckRedirect: func(req *http.Request, via []*http.Request) error {
			req.Header = via[len(via)-1].Header.Clone() // G119: copies all headers including Authorization/Cookie
			return nil
		},
	}
}

func main() {
	c := client()
	resp, err := c.Get("https://example.com/redirect")
	if err != nil {
		return
	}
	defer resp.Body.Close()
}
