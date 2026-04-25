// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-016: integer downcast after strconv parse

package main

import (
	"fmt"
	"strconv"
)

func parsePort(s string) uint16 {
	// TRIGGERS VNX-GO-016: Atoi result immediately cast to uint16 - truncates values > 65535
	n, _ := strconv.Atoi(s)
	return uint16(n)
}

func parseIndex(s string) int8 {
	// TRIGGERS VNX-GO-016: ParseInt 64-bit result cast to int8 - silently truncates
	n, _ := strconv.ParseInt(s, 10, 64)
	return int8(n)
}

func parseCount(s string) uint32 {
	// TRIGGERS VNX-GO-016: ParseUint result narrowed to uint32
	n, _ := strconv.ParseUint(s, 10, 64)
	return uint32(n)
}

func main() {
	fmt.Println(parsePort("99999"))  // would silently truncate to 34463
	fmt.Println(parseIndex("300"))   // would silently truncate to 44
}
