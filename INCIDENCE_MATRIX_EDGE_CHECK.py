# INCIDENCE_MATRIX_EDGE_CHECK.PY

# This program creates an incidence matrix
# and shows which vertices are connected to each edge.

# Example graph
vertices = 4
edges = [(0, 1), (1, 2), (2, 3)]

# Initialize matrix
incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(vertices)]

# Fill the matrix
for edge_index, (u, v) in enumerate(edges):
    incidence_matrix[u][edge_index] = 1
    incidence_matrix[v][edge_index] = 1

# Display matrix
print("Incidence Matrix:")
for row in incidence_matrix:
    print(row)

# Check connected vertices for each edge
print("\nVertices connected to each edge:")
for edge_index in range(len(edges)):
    connected_vertices = []

    # Check each row in the current edge column
    for vertex in range(vertices):
        if incidence_matrix[vertex][edge_index] == 1:
            connected_vertices.append(vertex)

    print(f"Edge {edge_index + 1}: {connected_vertices}")
