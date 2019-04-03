import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np 


# From Vectors
vectors = [
[0, 1],
[0, 2],
[2, 3],
[2, 4]
]

G = nx.DiGraph()
G.add_edges_from(vectors)
plt.title("From Vectors")
nx.draw_spring(G,with_labels=True)
plt.show()


# from numpy matrix
matrix = [
[0, 1, 1, 0, 0, ],
[0, 0, 0, 0, 0, ],
[0, 0, 0, 1, 1, ],
[0, 0, 0, 0, 0, ],
[0, 0, 0, 0, 0, ],
]
matrix = np.matrix(matrix)
G2 = nx.from_numpy_matrix(matrix, create_using=nx.MultiDiGraph)
G2.edges(data=True)
plt.title("From Matrix")
nx.draw_spring(G2,with_labels=True)
plt.show()


# Find parrents and children of nodes.
print("\nParrents:")
for node in G2.nodes():
	parrents = list(G2.predecessors(node))
	print(f"Parrents of {node} are {parrents}")

print("\nChildren:")
for node in G2.nodes():
	children = list(G2.successors(node))
	print(f"Children of {node} are {children}")


# Remove edge
G2.remove_edge(2,4)

# Add new edge
G2.add_edge(2,5)
plt.title("Removed and added new Edge.")
nx.draw_spring(G2, with_labels=True)
plt.show()