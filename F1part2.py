import Classes
import Parts
import seaborn as sb
import Functions
import networkx as nx
import matplotlib.pyplot as plt

setups = []
setup_filter = []
setup_teamscore = []

G = nx.DiGraph()

for y in range(len(setups)):
    setup_teamscore.append(setups[y].teamscore)

Functions.Top_100(setups, setup_filter)

Functions.add_nodes_from_setups(G, setup_filter)  # Chamo a função para adicionar nós dos setups
Functions.add_nodes_from_parts(G)  # Chamo a função para adicionar nós das partes

Functions.add_edges(G,setup_filter)
out_degrees = dict(G.out_degree())
max_out_degree = max(out_degrees.values())
edge_widths = [1.5 * out_degrees[edge[0]] / max_out_degree for edge in G.edges()]

# Calcular posições dos nós usando circular layout

positions = nx.circular_layout(G, scale=20.0)

# Desenhando o Digrafo

colors = ["lightblue" if n[1]['part'] else "red" for n in G.nodes(data=True)]
nx.draw(G, pos=positions, width=edge_widths, with_labels=True, node_size=300, node_color=colors, font_size=12, font_color='black', font_weight='bold')
plt.show()

sb.kdeplot(G.out_degree)
plt.show()



