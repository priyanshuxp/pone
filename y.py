PRACTICAL 4

Aim: Write a program to identify whether a graph is bipartite using two colours, and show the result for different graphs.

# 2nd graph
inuputdata = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2, 5],
    5: [3, 6],
    6: [5]
}

# 5th graph
inputdata2 = {
    1: [5, 6],
    2: [5, 6],
    3: [6],
    4: [5, 6],
    5: [1, 2, 4],
    6: [1, 2, 3, 4]
}

# 4th graph
inputdata3 = {
    1: [2, 3, 6],
    2: [1, 4, 6],
    3: [1, 5, 6],
    4: [2],
    5: [3, 6],
    6: [1, 2, 3, 5]
}


def bipartites(graph):
    colors = {}

    for node in graph:
        if node not in colors:
            queue = [(node, 0)]
            colors[node] = 0

            while len(queue) > 0:
                temp = queue.pop(0)
                current_node = temp[0]
                current_color = temp[1]

                for neighbor in graph[current_node]:
                    if neighbor not in colors:
                        opposite_color = 1 - current_color
                        colors[neighbor] = opposite_color
                        queue.append((neighbor, opposite_color))

                    elif colors[neighbor] == current_color:
                        return False, colors

    return True, colors


bipartite, assigned_colors = bipartites(inputdata3)

if bipartite:
    color_map = {
        0: "yellow",
        1: "red"
    }

    print("Bipartite.")

    for node in assigned_colors:
        color_code = assigned_colors[node]
        color_name = color_map[color_code]
        print("Node", node, ":", color_name)

else:
    print("NOT bipartite.")


# Plotting
import matplotlib.pyplot as plt

# positions
pos = {
    1: (0, 2),
    2: (-2, 1),
    3: (2, 1),
    4: (-3, 0),
    5: (3, 0),
    6: (0, 0)
}

# draw edges
for node in inputdata3:
    for neighbor in inputdata3[node]:
        if node < neighbor:
            x = [pos[node][0], pos[neighbor][0]]
            y = [pos[node][1], pos[neighbor][1]]
            plt.plot(x, y, color="black")

# draw nodes
for node in pos:
    x = pos[node][0]
    y = pos[node][1]

    if node in assigned_colors:
        if assigned_colors[node] == 0:
            color = "yellow"
        else:
            color = "red"
    else:
        color = "yellow"

    plt.scatter(
        x, y,
        s=1000,
        color=color,
        edgecolors="black"
    )

    plt.text(
        x, y, str(node),
        ha="center",
        va="center",
        fontsize=14
    )

plt.axis("off")
plt.show()

OUTPUT

NOT bipartite.

For input graph = inputdata2

# 5th graph
inputdata2 = {
    1: [5, 6],
    2: [5, 6],
    3: [6],
    4: [5, 6],
    5: [1, 2, 4],
    6: [1, 2, 3, 4]
}

bipartite, assigned_colors = bipartites(inputdata2)

if bipartite:
    color_map = {
        0: "yellow",
        1: "red"
    }

    print("Bipartite.")

    for node in assigned_colors:
        color_code = assigned_colors[node]
        color_name = color_map[color_code]
        print("Node", node, ":", color_name)

else:
    print("NOT bipartite.")

OUTPUT

Bipartite.
Node 1 : yellow
Node 5 : red
Node 6 : red
Node 2 : yellow
Node 4 : yellow
Node 3 : yellow

---

PRACTICAL 5

Aim: Find the shortest path from a given node with Dijkstra’s algorithm, compute the density of the network (2E / V(V−1) for an undirected graph), and identify the ego node, that is, the node with the highest degree.

1. Shortest Path

# Shortest path, density of graph, ego node
from collections import deque

adj_input = {
    1: [2, 3, 5],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2, 5],
    5: [1, 2, 3, 4]
}


def dijkstra(adj_input, start, end):
    distance = {
        node: float('inf')
        for node in adj_input
    }

    distance[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in adj_input[current]:
            new_distance = distance[current] + 1

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                queue.append(neighbor)

    return distance[end]


node1 = int(input("Enter first node: "))
node2 = int(input("Enter second node: "))

print("Shortest path", dijkstra(adj_input, node1, node2))

OUTPUT

Enter first node: 1
Enter second node: 5
Shortest path 1

2. Density of Graph

adj_input = {
    1: [2, 3, 5],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2, 5],
    5: [1, 2, 3, 4]
}


def density_graph(adj_input):
    V = len(adj_input)

    if V == 0 or V == 1:
        return 0.0

    edges = set()

    for node, neighbors in adj_input.items():
        for neighbor in neighbors:
            edge = tuple(sorted((node, neighbor)))
            edges.add(edge)

    E = len(edges)

    # Density == 2 * E / (V * (V - 1))
    density = (2 * E) / (V * (V - 1))

    return density


print("Graph density:", density_graph(adj_input))

OUTPUT

Graph density: 0.7

3. Ego Node

adj_input = {
    1: [2, 3, 5],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2, 5],
    5: [1, 2, 3, 4]
}

max_node = None
max_count = -1

for node, neighbors in adj_input.items():
    current_count = len(neighbors)

    if current_count > max_count:
        max_count = current_count
        max_node = node

print("Ego node:", max_node)
print("No of connected nodes:", max_count)

OUTPUT

Ego node: 5
No of connected nodes: 4

4. Graph Visualization with Ego Node Highlighted

import matplotlib.pyplot as plt

adj_input = {
    1: [2, 3, 5],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2, 5],
    5: [1, 2, 3, 4]
}

max_node = None
max_count = -1

for node, neighbors in adj_input.items():
    current_count = len(neighbors)

    if current_count > max_count:
        max_count = current_count
        max_node = node

print(f"Identified Ego node for plotting: {max_node}")

pos = {
    1: (0, 4),
    2: (4, 4),
    3: (0, 0),
    4: (4, 0),
    5: (2, 2)
}

plt.figure(figsize=(8, 6))
ax = plt.gca()

for node, neighbors in adj_input.items():
    for neighbor in neighbors:
        if node < neighbor:
            x1, y1 = pos[node]
            x2, y2 = pos[neighbor]

            ax.plot(
                [x1, x2],
                [y1, y2],
                color='gray',
                linewidth=2,
                alpha=0.7,
                zorder=1
            )

for node, (x, y) in pos.items():
    color = 'yellow' if node == max_node else 'lightblue'
    radius = 0.7 if node == max_node else 0.5

    circle = plt.Circle(
        (x, y),
        radius=radius,
        color=color,
        zorder=2
    )

    ax.add_patch(circle)

    ax.text(
        x, y, str(node),
        ha='center',
        va='center',
        color='black',
        fontsize=12,
        fontweight='bold',
        zorder=3
    )

min_x = min(p[0] for p in pos.values()) - 1
max_x = max(p[0] for p in pos.values()) + 1
min_y = min(p[1] for p in pos.values()) - 1
max_y = max(p[1] for p in pos.values()) + 1

ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)
ax.set_aspect('equal', adjustable='box')

plt.title('Graph Visualization with Ego Node Highlighted (matplotlib only)')
plt.axis('off')
plt.show()

OUTPUT

Identified Ego node for plotting: 5

---

PRACTICAL 6

Aim: Create sociograms for persons-by-persons and committee-by-committee networks, and construct one-mode and two-mode networks from employee–movie data using Python.

1. Employee–Movie Network

import pandas as pd

df = pd.read_csv(
    "data.csv",
    sep="\t",
    names=["emp", "movie"],
    usecols=[0, 1]
)

# Employee to Movies
employeeTomovies = df.groupby("emp")["movie"].apply(list)

for employee, movies in employeeTomovies.items():
    print(f"{employee}(employee) -> {movies}")

print("\n")

# Movie to Employees
movieToemployees = df.groupby("movie")["emp"].apply(list)

for movie, employees in movieToemployees.items():
    print(f"{movie}(movie) -> {employees}")

OUTPUT

Anurag(employee) -> ['Dark', 'JaldiTheLate', 'KGF']
Dhruv(employee) -> ['KGF', 'GuardianOfGalaxy', 'TheMenu']
OMKAR(employee) -> ['SALLAR', 'JaldiTheLate', 'Dark']
Prince(employee) -> ['Spiderman', 'GuardianOfGalaxy', 'Ravan']
Priyanshu(employee) -> ['WarMachine', 'Dark', 'Ramayan']
Ronit(employee) -> ['Spiderman', 'Ramayan', 'Ravan']
Soham(employee) -> ['JaldiTheLate', 'Ramayan', 'TheMenu']

Dark(movie) -> ['Anurag', 'OMKAR', 'Priyanshu']
GuardianOfGalaxy(movie) -> ['Dhruv', 'Prince']
JaldiTheLate(movie) -> ['Anurag', 'OMKAR', 'Soham']
KGF(movie) -> ['Anurag', 'Dhruv']
Ramayan(movie) -> ['Ronit', 'Priyanshu', 'Soham']
Ravan(movie) -> ['Ronit', 'Prince']
SALLAR(movie) -> ['OMKAR']
Spiderman(movie) -> ['Ronit', 'Prince']
TheMenu(movie) -> ['Dhruv', 'Soham']
WarMachine(movie) -> ['Priyanshu']

2. Employee–Movie Bipartite Graph

import matplotlib.pyplot as plt

employees = list(employeeTomovies.index)
movies = list(movieToemployees.index)

for employee in employees:
    for movie in employeeTomovies[employee]:
        plt.plot(
            [0, 1],
            [employees.index(employee), movies.index(movie)],
            'k-'
        )

plt.scatter(
    [0] * len(employees),
    range(len(employees)),
    color='blue',
    s=100
)

plt.scatter(
    [1] * len(movies),
    range(len(movies)),
    color='red',
    s=100
)

for i, employee in enumerate(employees):
    plt.text(-0.02, i, employee, ha='right', va='center')

for i, movie in enumerate(movies):
    plt.text(1.02, i, movie, ha='left', va='center')

plt.xticks([0, 1], ['Employees', 'Movies'])
plt.yticks([])
plt.title("Employee-Movie Bipartite Graph")
plt.xlim(-0.3, 1.3)
plt.show()

3. Employee and Movie Connections Using Sets

import pandas as pd
from collections import defaultdict

df = pd.read_csv(
    "data.csv",
    sep="\t",
    names=["emp", "movie"],
    usecols=[0, 1]
)

employeeToMovies = defaultdict(set)
movieToEmployees = defaultdict(set)

for i in range(len(df)):
    employee = df["emp"].iloc[i]
    movie = df["movie"].iloc[i]

    employeeToMovies[employee].add(movie)
    movieToEmployees[movie].add(employee)

for employee, movies in employeeToMovies.items():
    print(f"{employee}(employee) -> {movies}")

print("\n")

for movie, employees in movieToEmployees.items():
    print(f"{movie}(movie) -> {employees}")

4. One-Mode Employee and Movie Projections

employees = list(employeeToMovies)
movies = list(movieToEmployees)

print("employees", employees)
print("Movie", movies)

employeeConnections = defaultdict(dict)

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        emp1 = employees[i]
        emp2 = employees[j]

        commonMovie = employeeToMovies[emp1] & employeeToMovies[emp2]

        if commonMovie:
            count = len(commonMovie)

            employeeConnections[emp1][emp2] = count
            employeeConnections[emp2][emp1] = count

print("\nEmployee connections:")

for employee, connections in employeeConnections.items():
    print(f"{employee} -> {dict(connections)}")

movieConnections = defaultdict(dict)

for i in range(len(movies)):
    for j in range(i + 1, len(movies)):
        movie1 = movies[i]
        movie2 = movies[j]

        commonEmployee = movieToEmployees[movie1] & movieToEmployees[movie2]

        if commonEmployee:
            count = len(commonEmployee)

            movieConnections[movie1][movie2] = count
            movieConnections[movie2][movie1] = count

print("\nMovie connections:")

for movie, connections in movieConnections.items():
    print(f"{movie} -> {dict(connections)}")

---

PRACTICAL 7

Aim: Add a node attribute named "type" to the two-mode employee–movie network, where every employee has the type employee and every movie has the type movie.

import pandas as pd

df = pd.read_csv(
    "data.csv",
    sep="\t",
    names=["employee", "movie"]
)

nodes = {}

for employee in df["employee"].unique():
    nodes[employee] = "employee"

for movie in df["movie"].unique():
    nodes[movie] = "movie"

connections = []

for i in range(len(df)):
    employee = df["employee"].iloc[i]
    movie = df["movie"].iloc[i]

    connections.append((employee, movie))

print("Nodes with type attribute:")

for node, node_type in nodes.items():
    print(f"{node} -> type = {node_type}")

print("\nEmployee-Movie connections:")

for employee, movie in connections:
    print(f"{employee} -> {movie}")

OUTPUT

Nodes with type attribute:
Anurag -> type = employee
Dhruv -> type = employee
OMKAR -> type = employee
Prince -> type = employee
Priyanshu -> type = employee
Ronit -> type = employee
Soham -> type = employee
Dark -> type = movie
JaldiTheLate -> type = movie
KGF -> type = movie
GuardianOfGalaxy -> type = movie
TheMenu -> type = movie
SALLAR -> type = movie
Spiderman -> type = movie
Ravan -> type = movie
WarMachine -> type = movie
Ramayan -> type = movie

Employee-Movie connections:
Anurag -> Dark
Anurag -> JaldiTheLate
Anurag -> KGF
Dhruv -> KGF
Dhruv -> GuardianOfGalaxy
Dhruv -> TheMenu
OMKAR -> SALLAR
OMKAR -> JaldiTheLate
OMKAR -> Dark
Prince -> Spiderman
Prince -> GuardianOfGalaxy
Prince -> Ravan
Priyanshu -> WarMachine
Priyanshu -> Dark
Priyanshu -> Ramayan
Ronit -> Spiderman
Ronit -> Ramayan
Ronit -> Ravan
Soham -> JaldiTheLate
Soham -> Ramayan
Soham -> TheMenu

---

PRACTICAL 8

Aim: Find the weighted projection of the two-mode employee–movie network, showing how many movies each pair of employees have in common.

import pandas as pd
from collections import defaultdict

df = pd.read_csv(
    "data.csv",
    sep="\t",
    names=["employee", "movie"]
)

employeeToMovies = defaultdict(set)

for i in range(len(df)):
    employee = df["employee"].iloc[i]
    movie = df["movie"].iloc[i]

    employeeToMovies[employee].add(movie)

employees = list(employeeToMovies)
employeeConnections = defaultdict(dict)

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        emp1 = employees[i]
        emp2 = employees[j]

        commonMovies = employeeToMovies[emp1] & employeeToMovies[emp2]

        if commonMovies:
            weight = len(commonMovies)

            employeeConnections[emp1][emp2] = weight
            employeeConnections[emp2][emp1] = weight

print("Weighted Employee Projection:")

for employee, connections in employeeConnections.items():
    print(f"{employee} -> {dict(connections)}")

OUTPUT

Weighted Employee Projection:
Anurag -> {'Dhruv': 1, 'OMKAR': 2, 'Priyanshu': 1, 'Soham': 1}
Dhruv -> {'Anurag': 1, 'Prince': 1, 'Soham': 1}
OMKAR -> {'Anurag': 2, 'Priyanshu': 1, 'Soham': 1}
Priyanshu -> {'Anurag': 1, 'OMKAR': 1, 'Ronit': 1, 'Soham': 1}
Soham -> {'Anurag': 1, 'Dhruv': 1, 'OMKAR': 1, 'Priyanshu': 1, 'Ronit': 1}
Prince -> {'Dhruv': 1, 'Ronit': 2}
Ronit -> {'Prince': 2, 'Priyanshu': 1, 'Soham': 1}

---

PRACTICAL 9

Aim: Write a program to exhibit structural equivalence, automorphic equivalence and regular equivalence in a graph.

1. Structural Equivalence

from itertools import combinations


def structuralEquivalencePairs(graph):
    nodes = list(graph.keys())
    pairs = []

    for u, v in combinations(nodes, 2):
        neighbors_u = set(graph[u])
        neighbors_v = set(graph[v])

        if neighbors_u == neighbors_v:
            pairs.append((u, v))

    return pairs


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

graphbc = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

print("Structural Equivalence Pairs for graph 1:")
print(structuralEquivalencePairs(graph))

print("\nStructural Equivalence Pairs for graph 2:")
print(structuralEquivalencePairs(graph2))

print("\nStructural Equivalence Pairs for graph bc:")
print(structuralEquivalencePairs(graphbc))

OUTPUT

Structural Equivalence Pairs for graph 1:
[('B', 'C')]

Structural Equivalence Pairs for graph 2:
[('D', 'E'), ('F', 'G')]

Structural Equivalence Pairs for graph bc:
[]

2. Automorphic Equivalence

from itertools import combinations


def automorphicEquivalence(graph):
    nodes = list(graph.keys())
    pairs = []

    for u, v in combinations(nodes, 2):
        if len(graph[u]) == len(graph[v]):
            pairs.append((u, v))

    return pairs


graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

print("Automorphic Equivalence Pairs for Graph 1:")

for pair in automorphicEquivalence(graph1):
    print(pair)

print("\nAutomorphic Equivalence Pairs for Graph 2:")

for pair in automorphicEquivalence(graph2):
    print(pair)

OUTPUT

Automorphic Equivalence Pairs for Graph 1:
('A', 'B')
('A', 'C')
('B', 'C')

Automorphic Equivalence Pairs for Graph 2:
('B', 'C')
('D', 'E')
('D', 'F')
('D', 'G')
('E', 'F')
('E', 'G')
('F', 'G')

3. Regular Equivalence

from itertools import combinations


def regularEquivalencePairs(graph):
    nodes = list(graph.keys())
    pairs = []

    for u, v in combinations(nodes, 2):
        neighbors_u = graph[u]
        neighbors_v = graph[v]

        degrees_u = sorted([
            len(graph[nbr]) for nbr in neighbors_u
        ])

        degrees_v = sorted([
            len(graph[nbr]) for nbr in neighbors_v
        ])

        if degrees_u == degrees_v:
            pairs.append((u, v))

    return pairs


graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

graph3 = {
    'A': ['B', 'C', 'H', 'I'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C'],
    'H': ['A', 'I'],
    'I': ['H']
}

print("Regular Equivalence Pairs for Graph 1:")
print(regularEquivalencePairs(graph3))

OUTPUT

Regular Equivalence Pairs for Graph 1:
[('B', 'C'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'F'), ('E', 'G'), ('F', 'G')]