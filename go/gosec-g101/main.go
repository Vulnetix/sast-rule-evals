package main

import "fmt"

func main() {
	// G101: Hardcoded credentials
	password := "supersecret123"
	apikey := "AKIAIOSFODNN7EXAMPLE"
	secret := "my-jwt-signing-secret"
	fmt.Println(password, apikey, secret)
}
