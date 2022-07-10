# Programa que maneja expresiones sobre booleanos.
# Giancarlo Dente
# 15-10395

from __future__ import annotations
from enum import Enum
from tkinter import N
from typing import Any, Callable, Generic, Iterable, Iterator, Optional, List, TypeVar
from dataclasses import dataclass
from pymaybe import *
import sys
MIN_PYTHON = (3, 10)
assert sys.version_info >= MIN_PYTHON, f"requires Python {'.'.join([str(n) for n in MIN_PYTHON])} or newer"

A = TypeVar('A')
B = TypeVar('B')

def traverse_maybe(f : Callable[[A],Optional[B]], iter : Iterable[A]) -> Maybe[Iterable[B]]:
    xs = []
    for item in iter:
        y = f(item)
        if y is None:
            return maybe(None)
        xs.append(y)
    return maybe(xs)



setattr(Nothing,'fmap',lambda _1,_2: maybe(None))
setattr(Something,'fmap',lambda self,f: maybe(f(self.get())))
setattr(Nothing,'and_then',lambda _1,_2: maybe(None))
setattr(Something,'and_then',lambda self,f: f(self.get()))
setattr(maybe,'traverse',traverse_maybe)

maybe.traverse = staticmethod(maybe.traverse)

@dataclass
class Value():
    '''
    Representa un valor para el interprete.
    '''
    # 
    value : bool 

    def __init__(self,b:bool) -> None:
        self.value = b
    
    @staticmethod
    def lexToken(token : str) -> Optional[Value]:
        match token:
            case "true":
                return Value(True)
            case "false":
                return Value(False)
            case _:
                return None
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def __str__(self) -> str:
        return self.__repr__()


class Operator(Enum):
    '''
    Representa los operadores posibles
    '''
    AND   = 1
    OR    = 2
    IMPLY = 3
    NEG   = 4

    @staticmethod
    def lexToken(token: str) -> Optional[Operator]:
        match token:
            case "&":
                return Operator.AND
            case "|":
                return Operator.OR
            case "=>":
                return Operator.IMPLY
            case "^":
                return Operator.NEG
            case _:
                return None
    
    @staticmethod
    def precedence(op : Operator) -> int:
        '''
        Precedencia de operadores, entre mas alto mas fuerte bindea.
        '''
        match op:
            case Operator.AND:
                return 4
            case Operator.OR:
                return 4
            case Operator.IMPLY:
                return 1
            case Operator.NEG:
                return 9
    
    def __repr__(self) -> str:
        match self:
            case Operator.AND:
                return "&"
            case Operator.OR:
                return "|"
            case Operator.IMPLY:
                return "=>"
            case Operator.NEG:
                return "^"
    def __str__(self) -> str:
        return self.__repr__()


# Un token puede ser o un operador o un valor.
Token = Operator | Value

def lexToken(tk : str) -> Optional[Token]:
    tk_ : Optional[Token] = Operator.lexToken(tk)
    if tk_ is None:
        tk_ = Value.lexToken(tk)
    
    return tk_ 

@dataclass(init=True)
class Tree(Generic[A]):
    '''
    Arbol que nos ayudara a mostrar las cosas en notacion infija
    '''
    val : A
    l : Optional[Tree[A]]
    r : Optional[Tree[A]]


def show_tree(t : Tree[Token]) -> str:

    # retorna verdadero si `c`` necesita parentizarse
    def precedence_par(p : Operator, c : Token) -> bool:
        match (c):
            case (Operator()):
                return  Operator.precedence(p) > Operator.precedence(c)
            case _ :
                return False 

    def assoc_par(p : Operator,l : Token, r : Token) -> int:
        match (p,l,r):
            case (Operator.IMPLY,Operator.IMPLY,_):
                return -1
            case (Operator.AND,_,Operator.AND):
                return 1
            case (Operator.AND,_,Operator.OR):
                return 1
            case (Operator.OR,_,Operator.AND):
                return 1
            case (Operator.OR,_,Operator.OR):
                return 1
            case _:
                return 0

    def _show_tree(t : Tree[Token]) -> str:
        match t:

            # solo tenemos un unario, asi que por pereza solo matcheamos el unico operador
            # idealmente deberia ser toda una clase de operadores
            case Tree(Operator.NEG,l,_):
                return f"^ {_show_tree(l)}"
            
            # El resto de los operadores se comportan iwal
            case Tree(Operator(),l,r):
                a = ""
                b = assoc_par(t.val,l.val,r.val)
                if precedence_par(t.val,l.val) or b == -1:
                    a = f"({_show_tree(l)}) {str(t.val)}"
                else:
                    a = f"{_show_tree(l)} {str(t.val)}"
                if precedence_par(t.val,r.val) or b == 1:
                    a = f"{a} ({_show_tree(r)})"
                else:
                    a = f"{a} {_show_tree(r)}"

                return a
            case Tree(Value(v),_,_):
                return str(v)
            case _:
                return ""
    
    return _show_tree(t)



class Modo():
    '''
    Representa el modo de evaluacion o muestreo.
    '''

    class _Modo(Enum):
        PRE  = 1
        POST = 2

    def __init__(self,modo : Modo._Modo) -> None:
        self.mode = modo

    @staticmethod
    def lexToken(token: str) -> Optional[Modo]:
        match token:
            case "pre":
                return Modo(Modo._Modo.PRE)
            case "post":
                return Modo(Modo._Modo.POST)
            case _:
                return None

    def _eval_pre(self,tks : List[Token]) -> Optional[Value]:
        pila : List[bool] = []
        for token in reversed(tks):
            match (token,pila):
                case (Value(v),_):
                    pila.insert(0,v)
                case (Operator.NEG,[tk,*rest]):
                    pila = [not tk, *rest]
                case (Operator.AND,[l,r,*rest]):
                    pila = [l and r, *rest]
                case (Operator.OR,[l,r,*rest]):
                    pila = [l or r, *rest]
                case (Operator.IMPLY,[l,r,*rest]):
                    pila = [not l or r, *rest]
                case _:
                    return None
        
        try:
            assert (len(pila)==1)
        except AssertionError:
            return None
        return Value(pila[0])
    
    def _show_pre(self,tks : List[Token]) -> Optional[str]:
        
        pila : List[Tree[Token]] = []

        for token in reversed(tks):
            match (token,pila):
                case (Value(v),_):
                    pila.insert(0,Tree(Value(v),None,None))
                case (Operator.NEG,[tk,*rest]):
                    pila = [Tree(token,tk,None), *rest]
                case (_,[l,r,*rest]):
                    pila = [Tree(token,l,r), *rest]
                case _:
                    return None
        try:
            assert (len(pila)==1)
        except AssertionError:
            return None
        return show_tree(pila[0])

    def _eval_post(self,tks : List[Token]) -> Optional[Value]:
        pila : List[bool] = []
        for token in tks:
            match (token,pila):
                case (Value(v),_):
                    pila.insert(0,v)
                case (Operator.NEG,[tk,*rest]):
                    pila = [not tk, *rest]
                case (Operator.AND,[r,l,*rest]):
                    pila = [l and r, *rest]
                case (Operator.OR,[r,l,*rest]):
                    pila = [l or r, *rest]
                case (Operator.IMPLY,[r,l,*rest]):
                    pila = [not l or r, *rest]
                case _:
                    return None
        try:
            assert (len(pila)==1)
        except AssertionError:
            return None
        return Value(pila[0])

    def _show_post(self,tks : List[Token]) -> Optional[str]:
        
        pila : List[Tree[Token]] = []

        for token in tks:
            match (token,pila):
                case (Value(v),_):
                    pila.insert(0,Tree(Value(v),None,None))
                case (Operator.NEG,[tk,*rest]):
                    pila = [Tree(token,tk,None), *rest]
                case (_,[r,l,*rest]):
                    pila = [Tree(token,l,r), *rest]
                case _:
                    return None

        try:
            assert (len(pila)==1)
        except AssertionError:
            return None
        return show_tree(pila[0])

    
    def show(self,tks : List[Token]) -> Optional[str]:
        match self.mode:
            case Modo._Modo.PRE:
                return self._show_pre(tks)
            case Modo._Modo.POST:
                return self._show_post(tks)
            case _:
                return None
    
    
    def eval(self,tks : List[Token]) -> Optional[Value]:
        match self.mode:
            case Modo._Modo.PRE:
                return self._eval_pre(tks)
            case Modo._Modo.POST:
                return self._eval_post(tks)
            case _:
                return None

class Action():
    @staticmethod
    def lex_and_eval(stream : str) -> Optional[Value]:
        stream_ : List[str] = list(map(lambda x: x.strip(),stream.lower().split(sep=' ')))
        match stream_:
            case ["salir"]:
                raise InterruptedError
            case ["eval",mode,*args]:
                return maybe.traverse(lambda x: lexToken(x),args).and_then(lambda tks: 
                    maybe(Modo.lexToken(mode)).eval(tks)
                ).or_else(None)
            case ["mostrar",mode,*args]:
                return maybe.traverse(lambda x: lexToken(x),args).and_then(lambda tks: 
                    maybe(Modo.lexToken(mode)).show(tks)
                ).or_else(None)
            case _:
                return None 



def main():
    # pide repetidamente al usuario una accion para proceder.
    while True:
        i : str = input("- ")
        try:
            result = Action.lex_and_eval(i)
        except InterruptedError:
            return
    
        if result is None:
            print("Syntax Error")
        else:
            print(result)

if __name__=="__main__":
    main()
    

