class Pila<T> : Secuencia<T> {

    private var head : T?       = null
    private var tail : Pila<T>? = null

    override fun agregar(t: T) {
        if (this.vacio()){
            head = t
            return
        }

        val aux : Pila<T> = Pila<T>()
        aux.head = this.head
        aux.tail = this.tail
        this.head = t
        this.tail = aux
    }

    @Throws(RuntimeException::class)
    override fun remover(): T {
        if (this.vacio()){
            throw RuntimeException("Pila Vacia")
        }
        val head : T = this.head!!
        this.head = this.tail?.head
        this.tail = this.tail?.tail
        return head
    }

    override fun vacio(): Boolean {
        return this.head == null
    }

    override fun toString(): String {
        var aux : Pila<T> = this
        var s : String = ""

        while (!aux.vacio()){
            s = "$s ${aux.head!!.toString()} <-"
        }

        s = "$s null"
        return s
    }
}