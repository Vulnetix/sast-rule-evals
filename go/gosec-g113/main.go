package main

import "net/http"

// G113: HTTP request smuggling — conflicting Transfer-Encoding and Content-Length headers

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Transfer-Encoding", "chunked") // G113: conflicting headers enable request smuggling
	w.Header().Set("Content-Length", "100")
	w.Write([]byte("response body")) //nolint
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
