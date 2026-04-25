// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-015: WaitGroup.Add() called inside goroutine

package main

import (
	"fmt"
	"sync"
)

func processItems(items []string) {
	var wg sync.WaitGroup
	results := make([]string, 0)

	for _, item := range items {
		// TRIGGERS VNX-GO-015: wg.Add called inside the goroutine
		go func(s string) {
			wg.Add(1)  // race: Wait() may run before this Add() executes
			defer wg.Done()
			results = append(results, s)
		}(item)
	}

	wg.Wait()
	fmt.Println(results)
}

// Safe version: Add() called BEFORE launching the goroutine
func safeProcessItems(items []string) {
	var wg sync.WaitGroup
	for _, item := range items {
		wg.Add(1)
		go func(s string) {
			defer wg.Done()
			fmt.Println(s)
		}(item)
	}
	wg.Wait()
}
