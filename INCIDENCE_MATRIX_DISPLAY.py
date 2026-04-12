# INCIDENCE_MATRIX_DISPLAY.PY

# This program creates and displays the incidence matrix
# for a graph using the given number of vertices and edges.

# Number of vertices
vertices = 4

# List of edges as tuples: (start_vertex, end_vertex)
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

# Create an incidence matrix filled with 0
incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(vertices)]

# Fill the incidence matrix
for edge_index, (u, v) in enumerate(edges):
    incidence_matrix[u][edge_index] = 1
    incidence_matrix[v][edge_index] = 1

# Display the incidence matrix
print("Incidence Matrix:")
for row in incidence_matrix:
    print(row)
