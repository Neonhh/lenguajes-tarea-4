# Pregunta 1
Estudiante: Néstor Herrera
Carnet: 18-10796

## Cargando los modulos en el interprete

`irb`
`load 'Busqueda.rb'`

## Contenidos de archivos

**En Busqueda**
- Clase Busqueda
- Subclases de Busqueda, DFS y BFS
- Aqui se importan las dependencias de Grafo y Secuencia

**En Grafo**
Una implementacion de grafo usando listas de adyacencia, tomada de GeeksForGeeks.

**En Secuencia**
- Interfaz `Secuencia`
- Clases `Pila` y `Cola`

## Ejemplos de uso

```
# Crear grafo
grafo = Graph.new

# Añadir nodos
grafo.add_node(1)
grafo.add_node(2)
grafo.add_node(3)
grafo.add_node(4)
grafo.add_node(5)

# Añadir aristas
grafo.add_edge(1, 2)
grafo.add_edge(1, 3)
grafo.add_edge(2, 4)
grafo.add_edge(3, 4)
grafo.add_edge(4, 5)

# Ejemplos de busqueda

dfs = DFS.new(grafo)
resultado_dfs = dfs.buscar(1, 5) # Comienza la búsqueda en 1 y busca 6
puts "DFS resultado: #{resultado_dfs}" # => DFS resultado: 3 

bfs = BFS.new(grafo)
resultado_bfs = bfs.buscar(1, 5) # Comienza la búsqueda en 1 y busca 6
puts "BFS resultado: #{resultado_bfs}" # => BFS resultado: 6

deberia_dar_menos1 = bfs.buscar(4, 6) # Comienza la búsqueda en 4 y busca 6
puts "BFS resultado: #{deberia_dar_menos1}" # => BFS resultado: -1

```