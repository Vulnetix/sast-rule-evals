package main

import (
	"crypto/tls"
	"crypto/x509"
)

// G123: TLS resumption may bypass VerifyPeerCertificate when VerifyConnection is unset

func main() {
	_ = &tls.Config{
		// G123: VerifyPeerCertificate set but VerifyConnection absent — bypassed on TLS session resumption
		VerifyPeerCertificate: func(_ [][]byte, _ [][]*x509.Certificate) error { return nil },
	}
}
