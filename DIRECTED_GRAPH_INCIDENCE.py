# DIRECTED_GRAPH_INCIDENCE.PY

# This program creates the incidence matrix for a directed graph.
# For a directed edge:
# -1 represents the edge leaving a vertex
#  1 represents the edge entering a vertex

# Example directed graph
vertices = 4
edges = [(0, 1), (0, 2), (2, 3), (1, 3)]

# Create matrix with 0
incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(vertices)]

# Fill matrix for directed graph
for edge_index, (u, v) in enumerate(edges):
    incidence_matrix[u][edge_index] = -1  # edge goes out from u
    incidence_matrix[v][edge_index] = 1   # edge comes into v

# Print matrix
print("Incidence Matrix for Directed Graph:")
for row in incidence_matrix:
    print(row)
