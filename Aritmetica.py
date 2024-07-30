def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

def operaciones(nombre,n1,n2):
    print(nombre)
    print(15*"-")

    print("Sumar:",sumar(n1,n2))
    print("Restar:", restar(n1,n2))
    print("Multiplicar:",multiplicar(n1,n2))
    print("divicion:",dividir(n1,n2))
    print(15*"-")

def edad(nombres,edad):
    print(nombres,"tiene",edad)

edad("Jose",19)

# operaciones("Beyla",10,5)
# operaciones("Angel",10,15)