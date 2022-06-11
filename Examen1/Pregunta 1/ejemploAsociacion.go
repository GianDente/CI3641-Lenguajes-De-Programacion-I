package main

import "fmt"

var x = 1

func P(y int, t) {

	w := func(z) {
		x = y * z
	}

	var x = y * 2
	if y < 2 {
		P(y+2, w)
	} else if y < 4 {
		var x = 2
		P(y+x, t)
	} else {
		t(y)
	}
	fmt.Println(x, y)
}

func main() {
	P(x, P)
	fmt.Println(x)
}
