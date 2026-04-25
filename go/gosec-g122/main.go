package main

import (
	"io/fs"
	"os"
	"path/filepath"
)

// G122: Filesystem TOCTOU race — callback path used in destructive sink inside WalkDir

func main() {
	_ = filepath.WalkDir("/tmp", func(path string, d fs.DirEntry, err error) error {
		_ = d
		_ = err
		return os.Remove(path) // G122: TOCTOU — path used directly in os.Remove inside WalkDir
	})
}
