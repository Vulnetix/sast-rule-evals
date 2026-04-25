package main

import (
	"fmt"
	"os"
)

func main() {
	// G303: Creating file in shared tmp directory without ioutil.TempFile
	f, err := os.Create("/tmp/myapp-data.tmp")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	defer os.Remove(f.Name())
	fmt.Println(f.Name())
}
