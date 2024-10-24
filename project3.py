import matplotlib.pyplot as plt
import networkx as nx

# Define the cities (nodes) and coordinates
cities = {
    "Uppsala": (17.6389, 59.8586), 
    "Stockholm": (18.0686, 59.3293), 
    "Goteborg": (11.9746, 57.7089), 
    "Malmo": (13.0038, 55.6050),
    "Falun": (15.6319, 60.6036),
    "Ostersund": (14.6348, 63.1792),
    "Umea": (20.2630, 63.8258),
    "Lund": (13.1910, 55.7047)
}

# Define the edges (links between cities), including weights
edges = [
    ("Stockholm", "Goteborg", 25), 
    ("Stockholm", "Lund", 30), 
    ("Goteborg", "Malmo", 25),
    ("Stockholm", "Falun", 15),
    ("Falun", "Ostersund", 15),
    ("Ostersund", "Umea", 15)
]

# Step 1: Sort edges by weight
edges = sorted(edges, key=lambda x: x[2])

# Union-Find data structure for cycle detection
parent = {}
rank = {}

def find(node):
    # Find the root of the set in which element `node` is present
    if parent[node] != node:
        parent[node] = find(parent[node])  # Path compression
    return parent[node]

def union(node1, node2):
    # Union by rank
    root1 = find(node1)
    root2 = find(node2)
    
    if root1 != root2:
        # Attach smaller rank tree under root of higher rank tree
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

# Initialize the Union-Find structure
for city in cities:
    parent[city] = city
    rank[city] = 0

# Step 2: Kruskal's algorithm to find MST
mst_edges = []  # List to store the edges of the MST
for edge in edges:
    city1, city2, weight = edge
    
    # Check if adding this edge would form a cycle
    if find(city1) != find(city2):
        union(city1, city2)
        mst_edges.append((city1, city2, weight))

# Plotting the results
# Create a NetworkX graph
G = nx.Graph()
for city, coords in cities.items():
    G.add_node(city, pos=coords)
G.add_weighted_edges_from(edges)

# Extract positions from the graph
pos = nx.get_node_attributes(G, 'pos')

# Plot the original graph edges
fig, ax = plt.subplots(figsize=(10, 6))
nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)})

# Highlight the MST edges
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(u, v) for u, v, w in mst_edges], width=2.5, edge_color='red')

# Title and display
plt.title("Graph with Highlighted Minimum Spanning Tree (MST) Using Kruskal's Algorithm")
plt.axis('off')
plt.show()

# Output the MST edges
print("Minimum Spanning Tree edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (weight: {w})")
