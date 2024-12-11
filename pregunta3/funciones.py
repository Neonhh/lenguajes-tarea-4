class Clase:
    def __init__(self, metodos, superclase = None):
        self.metodos = metodos
        self.superclase = superclase
        
    def buscar_metodo(self, metodo):
        if metodo in self.metodos:
            return metodo
        elif clasesDefinidas.get(self.superclase) != None:
            return clasesDefinidas.get(self.superclase).buscar_metodo(metodo)
        else:
            return None
    
    def buscar_superclase(self, superclase):
        if clasesDefinidas.get(self.superclase) == superclase:
            return self
        elif clasesDefinidas.get(self.superclase) != None:
            return clasesDefinidas.get(self.superclase).buscar_superclase(superclase)
        else:
            return None

clasesDefinidas = {}
def clase_hereda(subclase, superclase, metodos):
    
    # Debe reportar error si la clase ya existe
    if existe(subclase):
        print(f"Error: La clase {subclase} ya existe")
        return
    
    # Debe reportar error si la clase super no existe
    if not existe(superclase):
        print(f"Error: La clase {superclase} no existe")
        return
    
    # Debe reportar error si se genera un ciclo en la jerarquia
    if clasesDefinidas[superclase].buscar_superclase(subclase) != None:
        print(f"Error: La clase {subclase} ya existe en la jerarquia")
        return
    
    # Debe reportar error si algun metodo esta repetido en la lista
    conteoMetodos = {}
    for metodo in metodos:
        if conteoMetodos.get(metodo) == None:
            conteoMetodos[metodo] = 1
        else:
            print(f"Error: El metodo {metodo} esta repetido")
            return
    
    clasesDefinidas[subclase] = Clase(metodos, superclase)

def clase_no_hereda(clase, metodos):

    # Debe reportar error si la clase ya existe
    if existe(clase):
        print(f"Error: La clase {clase} ya existe")
        return
    
    # Debe reportar error si algun metodo esta repetido en la lista
    conteoMetodos = {}
    for metodo in metodos:
        if conteoMetodos.get(metodo) == None:
            conteoMetodos[metodo] = 1
        else:
            print(f"Error: El metodo {metodo} esta repetido")
            return
    
    clasesDefinidas[clase] = Clase(metodos)


def describir(clase):
    print(f"Describiendo la clase {clase}")

    print("Metodo f: ", clasesDefinidas[clase].buscar_metodo("f"))
    print("Metodo g: ", clasesDefinidas[clase].buscar_metodo("g"))
    print("Metodo h: ", clasesDefinidas[clase].buscar_metodo("h"))
    print("Metodo i: ", clasesDefinidas[clase].buscar_metodo("i"))


def existe(nombre_clase):
    return nombre_clase in clasesDefinidas