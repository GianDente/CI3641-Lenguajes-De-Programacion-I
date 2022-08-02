class Cola<T> : Secuencia<T> {

    private var head : T?       = null
    private var tail : Cola<T>? = null

    override fun agregar(t: T) {
        if (this.vacio()){
            head = t
            return
        }

        if (this.tail == null){
            this.tail = Cola<T>()
            this.tail!!.agregar(t)
            return
        }

        this.tail!!.agregar(t)
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
        var aux : Cola<T> = this
        var s : String = ""

        while (!aux.vacio()){
            s = "$s ${aux.head!!.toString()} <-"
        }

        s = "$s null"
        return s
    }
}