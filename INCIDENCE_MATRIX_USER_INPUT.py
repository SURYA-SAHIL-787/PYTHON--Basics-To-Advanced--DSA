# INCIDENCE_MATRIX_USER_INPUT.PY

# This program takes graph details from the user
# and generates the incidence matrix.

# Get number of vertices and edges from the user
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

# Store edges
edges = []

# Take edge input
for i in range(edges_count):
    u = int(input(f"Enter start vertex of edge {i + 1}: "))
    v = int(input(f"Enter end vertex of edge {i + 1}: "))
    edges.append((u, v))

# Create incidence matrix with all 0s
incidence_matrix = [[0 for _ in range(edges_count)] for _ in range(vertices)]

# Fill the matrix
for edge_index, (u, v) in enumerate(edges):
    incidence_matrix[u][edge_index] = 1
    incidence_matrix[v][edge_index] = 1

# Print the matrix
print("\nIncidence Matrix:")
for row in incidence_matrix:
    print(row)
