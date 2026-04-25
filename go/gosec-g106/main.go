package main

import (
	"fmt"
	"golang.org/x/crypto/ssh"
)

func main() {
	// G106: SSH InsecureIgnoreHostKey
	config := &ssh.ClientConfig{
		User:            "user",
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}
	fmt.Println(config)
}
