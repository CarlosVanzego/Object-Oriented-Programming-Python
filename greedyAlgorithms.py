# Greedy Algorithms
# 
# A greedy algorithm always takes the best/cheapest option available at the moment, even if that might not be the best way to go from an overall point of view.
# Problems must exhibit two properties in order to implement a Greedy solution:
\
# Optimal Substructure
# A problem has an optimal substructure if an optimal solution to the entire problem contains the optimal solutions to the sub-problems.

# The Greedy Property
# An optimal solution is reached by "greedily" choosing the locally optimal choice without ever reconsidering previous choices.

# Prim's Algorithm
# Finds a minimum spanning tree for a weighted undirected graph. Prim's find a subset of edges that forms a tree that includes every node in the graph
# Time complexity: O(|V|^2)

# Kruskal's Algorithm
# Kruskal's Algorithm is alos a greedy algorithm that finds a minimum spanning tree in a graph, However, in Kruskal's, the graph does not have to be connected.
# Time complexity: O(|E|log|V|)