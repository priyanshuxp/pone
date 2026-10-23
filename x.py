Write a program to distinguish between a network as a
matrix, a network as an edge list, and a network as sociogram (or
"network graph") using 3 distinct networks representative of
each.
import numpy as np
import matplotlib.pyplot as plt
label = ["A", "B", "C", "D"]
# 1. Network as Matrix
A = np.array([
 [0,1,1,1],
 [1,0,1,1],
 [1,1,0,1],
 [1,1,1,0]
])
print("Network as Adjacency Matrix:")
print(A)
# 2. Network as Edge List
E = np.array([
 [0,1],
 [0,2],
 [0,3],
 [1,2],
 [1,3],
 [2,3]
])
print("\nNetwork as Edge List:")
for edge in E:
 print(label[edge[0]], "-", label[edge[1]])
# 3. Network as Sociogram / Network Graph
node_positions = {
 "A": (1,5),
 "B": (5,5),
 "C": (1,1),
 "D": (5,1)
}
plt.figure(figsize=(8,6))
# Draw edges
for edge in E:
 node1 = label[edge[0]]
 node2 = label[edge[1]]
 x1, y1 = node_positions[node1]
 x2, y2 = node_positions[node2]
 plt.plot([x1, x2], [y1, y2], "b")
# Draw nodes
for node, pos in node_positions.items():
 plt.scatter(
 pos[0],
 pos[1],
 s=100,
 color="skyblue",
 edgecolor="black"
 )
 plt.text(
 pos[0] + 0.1,
 pos[1] + 0.1,
 node,
 fontsize=12
 )
plt.title("Network Graph / Sociogram")
plt.axis("equal")
plt.axis("off")
plt.show()




2.Compute the following node level measures: (i) Density,
(ii) Degree, (iii) Reciprocity, (iv) Transitivity, (v) Centralization, (vi)
Clustering

import numpy as np
adjacency_matrix = np.array([
 [0, 1, 1, 1],
 [1, 0, 1, 1],
 [1, 1, 0, 1],
 [1, 1, 1, 0]
])
print("Adjacency Matrix:")
print(adjacency_matrix)
# Degree 
degrees = np.sum(adjacency_matrix, axis=1)
print("\nDegree of each node:")
for i, degree in enumerate(degrees):
 print(f"Node {i}: {degree}")
num_vertices = adjacency_matrix.shape[0]
num_edges = int(np.sum(adjacency_matrix) / 2)

print("\nNumber of edges:", num_edges)
# Density 
max_possible_edges = num_vertices * (num_vertices - 1) / 2
if max_possible_edges == 0:
 graph_density = 0.0
else:
 graph_density = num_edges / max_possible_edges
print("\nGraph Properties:")
print(f"Number of Vertices (V): {num_vertices}")
print(f"Number of Edges (E): {num_edges}")
print(f"Maximum possible edges: {int(max_possible_edges)}")
print(f"Graph Density: {graph_density:.4f}")

#********************Clustering********************
# Ci = no of edges between neighbors of Vi / no of maximum po
ssible edges between neighbors of Vi
#
# Ci = 2 * Ei / Ki(Ki - 1)
#
# Ei = actual number of edges between the neighbors of node V
i.
#
# Ki(Ki - 1) represents all potential edges between the neigh
bors
# in a complete graph.
#
# In an undirected graph, each edge is counted twice in the a
djacency matrix.
import numpy as np
adjacency_matrix = np.array([
 [0, 1, 1, 1],
 [1, 0, 1, 1],
 [1, 1, 0, 1],
 [1, 1, 1, 0]
])
for target_node in range(len(adjacency_matrix)):
 neighbors = np.where(adjacency_matrix[target_node] == 1)
[0]
numberOfNeighbor = len(neighbors) # Degree
 sub_matrix = adjacency_matrix[np.ix_(neighbors, neighbor
s)]
 two_E_i = np.sum(sub_matrix)
 if numberOfNeighbor >= 2:
 c_i = two_E_i / (numberOfNeighbor * (numberOfNeighbor
- 1))
 else:
 c_i = 0.0
 print(f"--- Node V{target_node} Analysis ---")
 print(f"Neighbors: {neighbors}")
 print(f"Number of neighbors (K_i): {numberOfNeighbor}")
 print(f"Clustering Coefficient (C_i): {c_i:.4f}")
 print()

