// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-014: Mutex Lock() without deferred Unlock()

package main

import "sync"

type Cache struct {
	mu   sync.Mutex
	data map[string]string
}

func (c *Cache) Set(key, value string) {
	// TRIGGERS VNX-GO-014: Lock() not immediately followed by defer Unlock()
	c.mu.Lock()
	// If the next line panics, the mutex is never unlocked
	c.data[key] = value
	c.mu.Unlock()
}

type ReadCache struct {
	rw   sync.RWMutex
	data map[string]string
}

func (r *ReadCache) Get(key string) string {
	// TRIGGERS VNX-GO-014: RLock() not followed by defer RUnlock()
	r.rw.RLock()
	val := r.data[key]
	r.rw.RUnlock()
	return val
}

// Safe version with defer:
func (c *Cache) SafeSet(key, value string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.data[key] = value
}
