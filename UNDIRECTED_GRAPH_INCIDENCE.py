# UNDIRECTED_GRAPH_INCIDENCE.PY

# This program builds the incidence matrix for an undirected graph.
# In an undirected graph, both connected vertices get value 1.

# Example graph
vertices = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]

# Initialize matrix with 0
incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(vertices)]

# Assign 1 for both vertices connected by each edge
for edge_index, (u, v) in enumerate(edges):
    incidence_matrix[u][edge_index] = 1
    incidence_matrix[v][edge_index] = 1

# Display result
print("Incidence Matrix for Undirected Graph:")
for row in incidence_matrix:
    print(row)
