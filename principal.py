from clases import Inventario as inv, ListadoInv as lst
listaInv = lst()

def menu():
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Eliminar Producto")
    print("4. Buscar por Codigo")
    print("5. Buscar por Nombre")
    print("6. Buscar por Precio")
    print("7. Mostrar Productos")
    print("10. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarRegistro():
    print("Agregar Datos del Producto")
    codigo = input("Código: ")
    nombres = input("Nombres: ")
    descripcion = input("Descripcion: ")
    precio = int(input("precio: "))
    minimo = int(input("Digite la existencia minima: "))
    existencia =int(input("digite la existencia del producto: "))
   
    inventario = inv(codigo, nombres, descripcion,precio,minimo,existencia)
    if existencia<minimo :
        print("La existencia es menor que la minima")
        print(inventario)
    else :
        print("la existencia es mayor que la minima")

    listaInv.agregarElemento(inventario)

def modificarRegistro():
    print("Editar Registro ")
    cod = input("Código: ")
    pro, pos = listaInv.buscarporCodigo(cod)
    print(f"""Nombres Actual: {pro.Nombres}
Precio actual: {pro.Precios}
Descripcion actual: {pro.Descripcion}""")

    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevoPrecio = int(input("Precio: "))
    nuevoDescripcions = input("Descripcion: ")
    nuevaExistencia= int(input("Existencia: "))
    nuevaMin= int(input("Minimo: "))
    newInv = inv(pro.Codigo,nuevoNombre,nuevoDescripcions,nuevoPrecio,nuevaExistencia,nuevaMin)
    listaInv.editarElemento(newInv, pos)

def eliminarRegistro():
    print("Eliminar Registro")
    cod = input("Código: ")
    inv, pos = listaInv.buscarporCodigo(cod)
    print(f"""Realmente desea eliminar el registro {inv}""")
    resp = input("SI - NO")
    if resp.upper()=="SI":
        listaInv.eliminarElemento(inv)
    else:
        print("Operación cancelada")


def buscarporCodigo():
    print("Buscar Registro")
    cod = input("Codigo: ")
    try:
        inv, pos = listaInv.buscarporCodigo(cod)
 
        if inv.Codigo != None:
            print(inv)
    except:
        print("Todo bien segui adelante")

def buscarporNombre():
    print("Buscar Registro")
    nom = input("Nombre: ")
    try:
        inv, pos = listaInv.buscarporNombre(nom)
 
        if inv.Nombres != None:
            print(inv)
    except:
        print("Todo bien segui adelante")
       
       
def buscarporPrecio():
    print("Buscar Registro")
    pre = int(input("Precio: "))
    try:
        inv, pos = listaInv.buscarporPrecio(pre)
 
        if inv.Precios != None:
            print(inv)
    except:
        print("Todo bien segui adelante")

def mostrarRegistros():
    for inventario in listaInv.lista:
        print(inventario)
        print("="*30)
   
def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: buscarporCodigo()
        elif op == 5: buscarporNombre()
        elif op == 6: buscarporPrecio()
        elif op == 7: mostrarRegistros()
        elif op == 10: print("hola papu")
        else: print("Opcion no valida")

main()

