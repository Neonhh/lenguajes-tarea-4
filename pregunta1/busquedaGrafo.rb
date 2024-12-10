=begin
i. Defina un interfaz o clase abstracta Secuencia, que represente una colección or-
denada de elementos. Debe tener los siguientes métodos:

• agregar: Recibe un elemento y lo agrega a la secuencia.
• remover: Devuelve un elemento de la secuencia y lo elimina de la misma.
Arroja un error si está vacía.
• vacio: Dice si la secuencia está vacía (no tiene elementos).
=end

module Secuencia
    def initialize(elementos)
        @elementos = elementos
    end
    
    def agregar(elemento)
        raise NotImplementedError
    end
    def remover
        raise NotImplementedError
    end
    def vacio?
        raise NotImplementedError
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
    def initialize(elementos = [])
        super(elementos)
    end

    def agregar(elemento)
        @elementos.push(elemento)
    end

    def remover
        @elementos.pop
    end

    def vacio?
        @elementos.empty?
    end
end



# Ejemplo de uso
pila = Pila.new
pila.agregar(1)
pila.agregar(2)
puts pila.remover # => 2
puts pila.vacio?   # => false

cola = Cola.new
cola.agregar(1)
cola.agregar(2)
puts cola.remover # => 1
puts cola.vacio?   # => false