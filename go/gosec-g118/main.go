package main

import (
	"context"
	"net/http"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	ctx := r.Context()
	_ = ctx
	// G118: goroutine uses context.Background() while request context exists — context leak
	go func() {
		child, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()
		_ = child
	}()
	w.Write([]byte("ok")) //nolint
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil) //nolint
}
