# ADVANCED ALGORITHMS:

# Topological Sort
# The topological sort algorithm takes a directed graph and returns an array of the nodes where each node appears before all the nodes it points to.
# Topological Sort is the linear ordering of a directed graph's nodes such that for every edge from the node u to node v, u comes before v in the ordering.
# It is a method to linearly order the vertices of a directed acyclic graph (DAG) such that for every edge from vertex "u" to vertex "v", "u" appears before "v" in the ordering; essentially, it provides a sequence of nodes where each node is visited only after all its dependencies (nodes that have edges pointing to it) have been visited. 

# Time Complexity: O(|V| + |E|)



# Dijkstra's Algorithm:
# Dijkstra's Algorithm is an algorithm for finding the shortest path between nodes in a graph;
# A graph traversal algorithm used to find the shortest path between a single source node and all other nodes in a graph.

# Time Complexity: O(|V|^2)



# Bellman-Ford Algorithm:
# Bellmman-Ford Algorithm is an algorithm that computes the shortest paths from a single source node to all other nodes in a weighted graph;
# It is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
# Although it is slower than Dijkstra's, it is more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

# Time Complexity:
# Best case: O(|E|)
# Worst case: O(|V||E|)