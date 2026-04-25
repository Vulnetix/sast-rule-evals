package main

import "fmt"

func main() {
	items := []struct{ val int }{{1}, {2}, {3}}
	ptrs := make([]*struct{ val int }, len(items))
	for i, v := range items {
		ptrs[i] = &v // G601: implicit memory aliasing in for loop
	}
	fmt.Println(ptrs)
}
