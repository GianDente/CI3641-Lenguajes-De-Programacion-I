// Programa que dados tres enteros no–negativos a, b y c , tal que c >= 2, calcula la potenciacion
// modulada a^b mod c.
// Giancarlo Dente
// 15-10395

package main

import "fmt"

func potenciacionMod(a int, b int, c int) int {

	var resultado int

	if b == 0 {
		resultado = 1
	} else if b > 0 {
		resultado = ((a % c) * potenciacionMod(a, b-1, c)) % c
	}

	return resultado
}

func main() {

	var a int
	var b int
	var c int

	fmt.Print("Introduzca el valor de a: ")
	fmt.Scanln(&a)
	fmt.Print("Introduzca el valor de b: ")
	fmt.Scanln(&b)
	fmt.Print("Introduzca el valor de c: ")
	fmt.Scanln(&c)

	if b >= 0 && c >= 2 {
		resultado := potenciacionMod(a, b, c)
		fmt.Printf("La potencia modulada %d^%d mod %d es igual a %d", a, b, c, resultado)
	} else {
		fmt.Println("Por favor introduzca un valor de b mayor o igual a 0 o un valor de c mayor o igual a 2")
		main()
	}

}
