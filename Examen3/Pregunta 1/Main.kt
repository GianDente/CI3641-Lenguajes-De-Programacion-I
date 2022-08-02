fun main(args: Array<String>) {

    val pila : Pila<Int> = Pila<Int>()
    val cola : Cola<Int> = Cola<Int>()

    println("Pila inicial vacia? ${pila.vacio()}")

    for (i in (0..3)){
        pila.agregar(i)
    }

    for (i in (0..3)){
        println("El tope de la pila es: ${pila.remover()}")
    }

    println("Pila final vacia? ${pila.vacio()}")

    try {
        pila.remover()
    } catch (e : RuntimeException){
        println("Excepcion de pila vacia capturada")
    }


    println("------------------------------------------------------")
    println("Cola inicial vacia? ${cola.vacio()}")

    for (i in (0..3)){
        cola.agregar(i)
    }

    for (i in (0..3)){
        println("El tope de la cola es: ${cola.remover()}")
    }

    println("cola final vacia? ${cola.vacio()}")

    try {
        cola.remover()
    } catch (e : RuntimeException){
        println("Excepcion de cola vacia capturada")
    }

}