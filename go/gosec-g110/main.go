package main

import (
	"compress/gzip"
	"io"
	"os"
)

func main() {
	// G110: Decompression bomb — io.Copy without limit
	f, err := os.Open("archive.gz")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	gr, err := gzip.NewReader(f)
	if err != nil {
		panic(err)
	}
	defer gr.Close()

	// Vulnerable: no io.LimitReader to cap output size
	io.Copy(os.Stdout, gr)
}
