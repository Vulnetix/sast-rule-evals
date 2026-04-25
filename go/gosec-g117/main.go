package main

import "encoding/json"

type User struct {
	Username string `json:"username"`
	Password string `json:"password"` // G117: sensitive field in JSON
	APIKey   string `json:"api_key"`  // G117: sensitive field in JSON
}

func main() {
	u := User{Username: "admin", Password: "secret", APIKey: "key123"}
	data, _ := json.Marshal(u)
	_ = data
}
