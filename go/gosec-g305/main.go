package main

import (
	"archive/zip"
	"fmt"
	"os"
	"path/filepath"
)

func extractZip(src, dest string) error {
	r, err := zip.OpenReader(src)
	if err != nil {
		return err
	}
	defer r.Close()

	for _, f := range r.File {
		// G305: Archive entry path not sanitized — traversal risk
		outPath := filepath.Join(dest, f.Name)
		if f.FileInfo().IsDir() {
			os.MkdirAll(outPath, 0755)
			continue
		}
		outFile, err := os.Create(outPath)
		if err != nil {
			return err
		}
		defer outFile.Close()
		fmt.Println("extracted:", outPath)
	}
	return nil
}

func main() {
	extractZip("archive.zip", "/tmp/output")
}
