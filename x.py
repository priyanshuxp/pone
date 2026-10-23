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
Untitled 1 [1,3],
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
Untitled 2 s=100,
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