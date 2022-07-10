# Iterador que recibe un numero n y genera todas las expresiones bien parentizadas que se pueden formar con n parentesis 
# de cada tipo.
# Giancarlo Dente
# 15-10395

# Haciendo uso de los iteradores del inciso anterior.
def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    acc = []
    if ls:
        for m in misterio(ls[1:]):
            for i in ins(ls[0], m):
                if i in acc:
                    pass
                else:
                    acc.append(i)
                    yield i
    else:
        yield []

def bienParentizadoAux(array):
    stack = []
    for i in array:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def bienParentizadas(n):
    parentesis = ""
    for i in range(n):
        parentesis += "("
        parentesis += ")"
    
    for m in misterio(parentesis):
        if bienParentizadoAux(m):
            yield m
        else:
            pass

for c in bienParentizadas(3):
    print (c)
