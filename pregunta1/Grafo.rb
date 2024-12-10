# Extraido de https://www.geeksforgeeks.org/how-to-implement-graph-in-ruby/#types-of-graphs
class Graph
  def initialize
    @nodes = Hash.new { |hash, key| hash[key] = [] }
  end

  def add_node(value)
    raise ArgumentError, "Node value cannot be nil" if value.nil?
    @nodes[value]
  end

  def add_edge(node1, node2)
    raise ArgumentError, "Nodes #{node1} and #{node2} 
    do not exist" unless @nodes[node1] && @nodes[node2]
    @nodes[node1] << node2
    
    # For undirected graphs, add the edge in the opposite 
    # direction as well
    @nodes[node2] << node1
  end

  def print_graph
    @nodes.each do |node, neighbors|
      puts "#{node} => #{neighbors.join(', ')}"
    end
  end
end