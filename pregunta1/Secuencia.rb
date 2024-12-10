=begin
i. Defina un interfaz o clase abstracta Secuencia, que represente una colección or-
denada de elementos. Debe tener los siguientes métodos:

• agregar: Recibe un elemento y lo agrega a la secuencia.
• remover: Devuelve un elemento de la secuencia y lo elimina de la misma.
Arroja un error si está vacía.
• vacio: Dice si la secuencia está vacía (no tiene elementos).
=end

# En el modulo se define un constructor para las clases que lo usan
# Y la funcion vacio?s que dice si la secuencia esta vacia
# Ademas las partes de otras funciones que sean iguales entre clases.
# En el caso de agregar, esta depende totalmente de la clase, asi que si
# No esta implementado en la clase se devuelve un error.
module Secuencia
    attr_reader :elementos
    def initialize(elementos = [])
        @elementos = elementos
    end
    
    def agregar(elemento)
        raise NotImplementedError
    end
    def remover
        raise "Secuencia vacia" if vacio?
    end
    def vacio?
        @elementos.empty?
    end
end

=begin
Defina dos clases concretas Pila y Cola que sean subtipo de Secuencia
• Para Pila los elementos se manejan de tal forma que el último en ser agregado
es el primero en ser removido.

• Para Cola los elementos se manejan de tal
=end

class Pila
    include Secuencia

    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        super()
        @elementos.pop
    end
end

class Cola
    include Secuencia

    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        super()
        @elementos.shift
    end
end