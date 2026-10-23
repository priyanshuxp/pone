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

Degree and density 
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
# Ci = no of edges between neighbors of Vi / no of maximum possible edges between neighbors of Vi
#
# Ci = 2 * Ei / Ki(Ki - 1)
#
# Ei = actual number of edges between the neighbors of node Vi.
#
# Ki(Ki - 1) represents all potential edges between the neighbors
# in a complete graph.
#
# In an undirected graph, each edge is counted twice in the adjacency matrix.

import numpy as np

adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

for target_node in range(len(adjacency_matrix)):
    neighbors = np.where(adjacency_matrix[target_node] == 1)[0]
    numberOfNeighbor = len(neighbors)  # Degree

    sub_matrix = adjacency_matrix[np.ix_(neighbors, neighbors)]
    two_E_i = np.sum(sub_matrix)

    if numberOfNeighbor >= 2:
        c_i = two_E_i / (numberOfNeighbor * (numberOfNeighbor - 1))
    else:
        c_i = 0.0

    print(f"--- Node V{target_node} Analysis ---")
    print(f"Neighbors: {neighbors}")
    print(f"Number of neighbors (K_i): {numberOfNeighbor}")
    print(f"Clustering Coefficient (C_i): {c_i:.4f}")
    print()


#********************Reciprocity********************
# Reciprocity = total number of reciprocal pairs in graph G
# / total number of pairs
#
# A reciprocal pair exists when:
# Vi -> Vj and Vj -> Vi

import numpy as np

reciprocity_matrix = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
])

reciprocal_pairs = 0
total_pairs = 0

for i in range(len(reciprocity_matrix)):
    for j in range(i + 1, len(reciprocity_matrix[i])):
        total_pairs += 1

        if reciprocity_matrix[i][j] == 1 and reciprocity_matrix[j][i] == 1:
            reciprocal_pairs += 1

reciprocity_ratio = reciprocal_pairs / total_pairs

print("Reciprocal Pairs:", reciprocal_pairs)
print("Total Pairs:", total_pairs)
print("Reciprocity:", reciprocity_ratio)


#********************Transitivity********************
# Transitivity = number of closed triplets
# / total number of triplets
#
# A triplet is closed when the three nodes are connected
# to each other and form a triangle.

import numpy as np

adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

closed_triplets = 0
total_triplets = 0
n = len(adjacency_matrix)

for i in range(n):
    neighbors = np.where(adjacency_matrix[i] == 1)[0]

    for j in range(len(neighbors)):
        for k in range(j + 1, len(neighbors)):
            node1 = neighbors[j]
            node2 = neighbors[k]

            total_triplets += 1

            if adjacency_matrix[node1][node2] == 1:
                closed_triplets += 1

transitivity = closed_triplets / total_triplets

print("Closed Triplets:", closed_triplets)
print("Total Triplets:", total_triplets)
print("Transitivity:", transitivity)


#********************Centralization********************
# Degree Centralization =
# Sum of differences between maximum degree and
# degree of each node / maximum possible centralization

import numpy as np

adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

degrees = np.sum(adjacency_matrix, axis=1)
maximum_degree = np.max(degrees)
n = len(adjacency_matrix)
sum_difference = 0

for degree in degrees:
    sum_difference += maximum_degree - degree

maximum_possible = (n - 1) * (n - 2)
centralization = sum_difference / maximum_possible

print("Degree of each node:", degrees)
print("Maximum Degree:", maximum_degree)
print("Centralization:", centralization)




Represent a network using single mode and double mode
data. Compute the adjacency matrix, degree diagonal matrix,
Laplacian matrix, transition probability matrix, and incidence
matrix.

# Import one mode/two mode dataset
import pandas as pd
import numpy as np

# Reading csv file
data = pd.read_csv('friendships.csv', index_col=0)
print(data)

# Removing headers names to get adjacency matrix itself which
# will be integer value
A = data.values
labels = data.index.to_list()

print("Adjacency matrix A \n", A)

# Find degree of each node
deg = np.sum(A, axis=1)
print("Degree \n", deg)

# Place degree values in diagonal in matrix
D = np.diag(deg)
print("Matrix after placing degree to diagonal D \n", D)

# Find laplacian matrix by subtracting adjacency matrix from
# degree matrix (L = D - A)
L = D - A
print("Laplacian matrix L \n", L)

# Transition Probability matrix -> divide Adjacency matrix with degree value row-wise
# for row wise just vchange degree from 1x4 to 4x1 matrix using np.newaxis
degree = deg[:, np.newaxis]
print("Degree 4x1 matrix \n", degree)

P = A / degree

# Replace NaN values with 0
# P = np.nan_to_num(P, copy=True, nan=0.0)

print("Transition probability matrix P \n", P)

# To find incidence matrix first we have to find edgelist
edgelist = []
n_nodes = A.shape[0]

for i in range(n_nodes):
    for j in range(i + 1, n_nodes):  # Avoid duplicate edges and self-loops
        if A[i, j] == 1:
            edgelist.append((labels[i], labels[j]))

print("Edgelist: ", edgelist)

# Incidence Matrix
n_edges = len(edgelist)
incidence_matrix = np.zeros((n_nodes, n_edges), dtype=int)
node_to_index = {label: i for i, label in enumerate(labels)}

for col_idx, (node1, node2) in enumerate(edgelist):
    row_idx1 = node_to_index[node1]
    row_idx2 = node_to_index[node2]

    incidence_matrix[row_idx1, col_idx] = 1
    incidence_matrix[row_idx2, col_idx] = 1

print("Incidence Matrix: \n", incidence_matrix)