class Clase:
    def __init__(self, metodos, superclase = None):
        self.metodos = metodos
        self.superclase = superclase
        
    def buscar_metodo(self, metodo):
        if metodo in self.metodos:
            return metodo
        elif self.superclase != None:
            return self.superclase.buscar_metodo(metodo)
        else:
            return None
    
    def buscar_superclase(self, superclase):
        if self.superclase == superclase:
            return self
        elif self.superclase != None:
            return self.superclase.buscar_superclase(superclase)
        else:
            return None

clasesDefinidas = {}
def clase_hereda(subclase, superclase, metodos):
    print(f"Creando clase {subclase} que hereda de {superclase} con los metodos {metodos}")
    
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
    
    # Debe reportar error si algun metodo esta repetido en la jerarquia
    metodos_unicos = set(metodos)
    for metodo in metodos_unicos:
        if clasesDefinidas[superclase].buscar_metodo(metodo) != None:
            print(f"Error: El metodo {metodo} ya existe en la jerarquia")
            return
    
    metodos = list(metodos_unicos)
    
    clasesDefinidas[subclase] = Clase(metodos, superclase)

def clase_no_hereda(clase, metodos):
    print(f"Creando clase {clase} con los metodos {metodos}")

    # Debe reportar error si la clase ya existe
    if existe(clase):
        print(f"Error: La clase {clase} ya existe")
        return
    
    clasesDefinidas[clase] = Clase(metodos)


def describir(clase):
    print(f"Describiendo la clase {clase}")

def existe(nombre_clase):
    return nombre_clase in clasesDefinidas