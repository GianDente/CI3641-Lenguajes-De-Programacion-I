interface Secuencia<T>
{
    abstract fun agregar(t : T)
    abstract fun remover() : T
    abstract fun vacio() : Boolean
}