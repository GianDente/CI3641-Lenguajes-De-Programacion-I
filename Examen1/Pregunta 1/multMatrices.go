// Programa que dadas dos matrices A y B, calcula su producto A x B
// Giancarlo Dente
// 15-10395

package main

import "fmt"

func main() {
	var A [20][20]int
	var B [20][20]int
	var C [20][20]int

	var N int
	var M int
	var P int
	var i int
	var j int
	var k int
	var count int

	count = 0

	fmt.Print("Introduzca el numero de filas de la matriz A: ")
	fmt.Scanln(&N)
	fmt.Print("Introduzca el numero de columnas/filas de la matriz A/B: ")
	fmt.Scanln(&M)
	fmt.Print("Introduzca el numero de columnas de la matriz B: ")
	fmt.Scanln(&P)

	fmt.Println("Introduzca los elementos de la matriz A: ")
	for i = 0; i < N; i++ {
		for k = 0; k < M; k++ {
			fmt.Scan(&A[i][k])
		}
	}

	fmt.Println("Introduzca los elementos de la matriz B: ")
	for k = 0; k < M; k++ {
		for j = 0; j < P; j++ {
			fmt.Scan(&B[k][j])
		}
	}

	for i = 0; i < N; i++ {
		for j = 0; j < P; j++ {
			for k = 0; k < M; k++ {
				count = count + A[i][k]*B[k][j]
			}
			C[i][j] = count
			count = 0
		}
	}

	fmt.Println("La matriz C=AxB es: ")
	for i = 0; i < N; i++ {
		for j = 0; j < P; j++ {
			fmt.Print(C[i][j], "\t")
		}
		fmt.Print("\n")
	}
}
