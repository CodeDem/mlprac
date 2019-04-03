# pip install networkx
# importing the networkx library 
import networkx as nx 
from pprint import pprint

# importing the matplotlib library for plotting the graph 
import matplotlib.pyplot as plt 

G= nx.erdos_renyi_graph(10, 0.5, directed = True) 
nx.draw_circular(G, with_labels=True) 
plt.show()
pgrank=nx.pagerank(G) 
print("Page Rank values of Random Graph")
pprint(pgrank)