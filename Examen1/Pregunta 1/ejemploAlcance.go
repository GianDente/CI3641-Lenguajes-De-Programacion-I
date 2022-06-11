package main

import "fmt"

var a = 1

func P() {
	a = 3
}

func Q() {
	var a = 2
	P()
	fmt.Println("valor de la variable a luego de llamar a P: a =", a)
}

func main() {
	Q()

	fmt.Println("a =", a)
}
