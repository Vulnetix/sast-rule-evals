// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-013: Go zip/tar slip via archive entry name

package main

import (
	"archive/tar"
	"io"
	"os"
	"path/filepath"
)

func extractTarUnsafe(tarFile string, destDir string) error {
	f, _ := os.Open(tarFile)
	defer f.Close()

	tr := tar.NewReader(f)
	for {
		header, err := tr.Next()
		if err == io.EOF {
			break
		}

		// VULNERABLE: header.Name used directly in filepath.Join without validation
		// An attacker can craft entries with "../" to escape destDir
		targetPath := filepath.Join(destDir, header.Name)

		outFile, _ := os.Create(targetPath)
		io.Copy(outFile, tr)
		outFile.Close()
	}
	return nil
}
