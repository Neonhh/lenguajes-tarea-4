# Guarda los metodos y superclases de cada clase
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

# Diccionario de clases definidas con sus respectivos metodos y superclases
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

    # Debe reportar error si la clase no existe
    if not existe(clase):
        print(f"Error: La clase {clase} no existe")
        return
    
    clase_descrita = clasesDefinidas[clase]

    # Metodos definidos en la misma clase
    for metodo in clase_descrita.metodos:
        print(f"{metodo} -> {clase} :: {metodo}")
    
    # Metodos heredados
    metodos_superclases(clasesDefinidas[clase].superclase, clase_descrita.metodos)

def existe(nombre_clase):
    return nombre_clase in clasesDefinidas

# Imprime recursivamente los metodos de las superclases que no se hayan impreso ya
def metodos_superclases(superclase, ya_visto = []):

    superclaseObj = clasesDefinidas.get(superclase)

    if superclaseObj == None: return

    for metodo in superclaseObj.metodos:
        if metodo not in ya_visto:
            ya_visto.append(metodo)
            print(f"{metodo} -> {superclase} :: {metodo}")
        
    return metodos_superclases(clasesDefinidas[superclase].superclase, ya_visto)
