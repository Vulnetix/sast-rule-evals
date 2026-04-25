package main

import "golang.org/x/crypto/ssh"

// G408: Stateful misuse of ssh.PublicKeyCallback — captures outer variable

var lastKey ssh.PublicKey

func setupServer() {
	config := &ssh.ServerConfig{}
	config.PublicKeyCallback = func(conn ssh.ConnMetadata, key ssh.PublicKey) (*ssh.Permissions, error) {
		lastKey = key // G408: writes captured outer variable inside PublicKeyCallback
		return &ssh.Permissions{}, nil
	}
	_ = config
}

func main() {
	setupServer()
}
