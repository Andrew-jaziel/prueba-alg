class Inventario:

    def __init__(self, cod, nom, des, pre,min,exis):
        self.Codigo = cod
        self.Descripcion= des
        self.Nombres = nom
        self.Precios = pre
        self.Existencia = exis
        self.Minimo = min #Becado sera un valor booleano
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Descripcion:{self.Descripcion}
Precios: {self.Precios}
Existencia: {self.Existencia}
Minimo: {self.Minimo}

"""

class ListadoInv:

    def __init__(self):
        self.lista =[]
    
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))
        
    def editarElemento(self, dato, pos):
        try:
            self.lista[pos]=dato
        except Exception as ex:
             print("Ocurrio un erro al editar:", str(ex))
    
    def eliminarElemento(self, pos):
        try:
            self.lista.remove(pos)
        except Exception as ex:
            print("Error al eliminar:", str(ex))
    
    def buscarporCodigo(self, cod):
        try:
            pos = 0
            for inv in self.lista:
                
                if inv.Codigo == cod:
                    print("Producto encontrado...")
                    return inv, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarporNombre(self, nom):
        try:
            pos = 0
            for inv in self.lista:
                
                if inv.Nombres == nom:
                    print("Producto encontrado...")
                    return inv, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarporPrecio(self,pre):
        try:
            pos = 0
            for inv in self.lista:
                
                if inv.Precios == pre:
                    print("Producto encontrado...")
                    return inv, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))


  