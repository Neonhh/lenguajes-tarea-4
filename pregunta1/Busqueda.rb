require './Secuencia.rb'

=begin
ii. Defina un tipo de datos que represente grafos como listas de adyacencias y cada
nodo sea representado por un número entero (puede usar todas las librerías a su
disposición en el lenguaje).
=end
# Seguramente esto cuenta como libreria, no? :clueless:
require './Grafo.rb'
#Igual hay que agregar un parche
class Graph
    # Esto permite acceder a la lista de adyacencias facilmente desde Busqueda
    def [](key)
        @nodes[key]
    end
end

=begin
Además, defina una clase abstracta Busqueda que debe tener un método buscar.
Este método debe recibir dos enteros: D y H, y debe devolver la cantidad de nodos
explorados, partiendo desde el nodo D hasta llegar al nodo H. En caso de que H no
sea alcanzable desde D, debe devolver el valor -1 (menos uno).
Esta clase debe estar parcialmente implementada, dejando solamente abstraído el
orden en el que se han de explorar los nodos.
=end

# Esto pudo implementarse como clase o como interfaz (modulo), pero como no se dijo
# explicitamente que se puede definir como interfaz, lo defini como clase XD
# El grafo y la secuencia (Pila o Cola) son provistos por DFS o BFS, en este caso subclases
# Mientras que Busqueda se encarga de llevar control de los nodos visitados
# Y devolver su cantidad al llegar a un destino (o -1 si no llega)
class Busqueda

    def initialize(grafo, secuencia)
        @grafo = grafo
        @secuencia = secuencia
        @visitados = {}
    end

    def buscar(inicio, fin)
        @secuencia.agregar(inicio)

        until @secuencia.vacio?
            elemento = @secuencia.remover
            next if @visitados[elemento]
            
            @visitados[elemento] = true
            return @visitados.size if elemento == fin
            
            @grafo[elemento].each do |vecino|
                @secuencia.agregar(vecino)
            end
        end

        return -1
    end

end

=begin
Defina dos clases concretas DFS y BFS que sean subtipo de Busqueda.
• Para DFS el orden de selección de nodos es a profundidad (usando un pila).
• Para BFS el orden de selección de nodos es a amplitud (usando un cola).
=end

class DFS < Busqueda
    def initialize(grafo)
        super(grafo, Pila.new)
    end
end

class BFS < Busqueda
    def initialize(grafo)
        super(grafo, Cola.new)
    end
end