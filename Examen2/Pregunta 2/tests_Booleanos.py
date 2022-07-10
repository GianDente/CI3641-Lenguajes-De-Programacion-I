from Booleanos import Action
import pytest
from pymaybe import *

def test_salir():
    with pytest.raises(InterruptedError):
        Action.lex_and_eval("SALIR")

def test_lex_errors():
    bad_first0 = "comando PRE | 1 2"
    bad_first1 = "mal POST 1 2 |"
    bad        = "asdf gkgk "
    bad2        = "asdf"
    empty      = ""
    empty2     = "           "
    empty_tab  = "\t"
    bad_mode0   = "MOSTRAR COSO | true false"
    bad_mode1   = "EVAL COSO | true false"
    bad_operand0 = "EVAL PRE | 1 true"
    bad_operand1 = "EVAL POST false 2 &"
    bad_operand2 = "EVAL POST false true ="
    bad_operand3 = "EVAL POST false djfng &"

    pred = lambda x : Action.lex_and_eval(x) is None 

    bads = [bad,bad2,bad_first0,bad_first1,empty,empty2,empty_tab,bad_mode0,bad_mode1,bad_operand0,bad_operand1,bad_operand2,bad_operand3]

    assert(all(map(pred,bads)))

    #assert(pred(bad_mode0))

def test_eval_errors():

    _1 = "EVAL POST true false true |"
    _2 = "EVAL PRE | true false true "
    _3 = "EVAL POST true false | true"
    _4 = "EVAL PRE true | false true "
    _5 = "MOSTRAR POST true false true |"
    _6 = "MOSTRAR PRE | true false true "
    _7 = "MOSTRAR POST true false | true"
    _8 = "MOSTRAR PRE true | false true "

    pred = lambda x : Action.lex_and_eval(x) is None 

    bads = [_1,_2,_3,_4,_5,_6,_7,_8]

    assert( all(map(pred,bads)))

def test_evaluations():
    _1 = "EVAL PRE | & => true true false true"
    _2 = "EVAL POST true false => false | true false ^ | &"
    _3 = "EVAL PRE => => => true true false false"
    _4 = "EVAL PRE => true => true => true false"
    _5 = "EVAL PRE | | false false false"
    _6 = "EVAL PRE | false | false false"

    f = lambda x: maybe(Action.lex_and_eval(x)).value.or_else(None)

    assert(f(_1) == True)
    assert(f(_2) == False)
    assert(f(_3) == True)
    assert(f(_4) == False)
    assert(f(_5) == False)
    assert(f(_6) == False)

def test_mostrar():
    _1 = "MOSTRAR PRE | & => true true false true"
    _2 = "MOSTRAR POST true false => false | true false ^ | &"
    _3 = "MOSTRAR PRE => => => true true false false"
    _4 = "MOSTRAR PRE => true => true => true false"
    _5 = "MOSTRAR PRE | | false false false"
    _6 = "MOSTRAR PRE | false | false false"

    f = lambda x: maybe(Action.lex_and_eval(x)).or_else(None)

    assert(f(_1) == "(True => True) & False | True")
    assert(f(_2) == "(True => False) | False & (True | ^ False)")
    assert(f(_3) == "((True => True) => False) => False")
    assert(f(_4) == "True => True => True => False")
    assert(f(_5) == "False | False | False")
    assert(f(_6) == "False | (False | False)")