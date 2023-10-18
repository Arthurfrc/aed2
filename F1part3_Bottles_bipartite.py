import matplotlib.pyplot as plt
import networkx as nx

data= [
["NAME","SPEED","CORNERING","POWER_UNIT","RELIABILITY","PIT_STOP","OVERTAKING","DEFENDING","RACE_START","TYRE_MANAGEMENT"],
    ["Aderencia",0,25,0,15,0,0,0,10,0],
    ["Arco_iris",20,0,0,0,0,0,25,5,0],
    ["Ballast",0,10,0,0,10,0,0,5,0],
    ["Butterfly",0,0,25,0,5,0,0,0,20],
    ["Caveira",25,0,10,0,0,15,0,0,0],
    ["Cranberry",0,0,0,10,0,20,20,0,0],
    ["Cuppa",0,20,0,0,0,10,0,20,0],
    ["Dead_Fast",25,0,20,0,0,0,0,0,5],
    ["Djinn",0,15,0,20,0,0,15,0,0],
    ["Downforce",0,5,0,0,0,0,15,0,15],
    ["Dragon",0,0,15,0,0,20,0,0,15],
    ["Eagle",0,0,0,15,15,0,0,0,20],
    ["Eclipse",25,0,0,0,10,15,0,0,0],
    ["Eggception",0,0,10,0,25,0,15,0,0],
    ["Eternal_Flame",0,0,0,15,0,25,0,0,10],
    ["Fogos",20,0,0,0,0,15,0,15,0],
    ["Frost",0,0,0,10,0,0,0,15,25],
    ["Gladiator",0,0,10,0,0,0,25,15,0],
    ["Herald",15,0,0,0,0,10,0,25,0],
    ["Hex",15,0,0,0,5,20,0,0,0],
    ["Instinct",0,0,15,5,0,0,0,10,0],
    ["Iron_Force",0,0,20,20,0,0,0,0,10],
    ["Kawaii",0,20,0,0,15,0,0,15,0],
    ["Lumberjack",0,0,0,25,0,0,15,0,10],
    ["Merlion",15,25,0,0,10,0,0,0,0],
    ["Movember",0,25,0,0,0,0,15,0,10],
    ["Nazar",0,0,0,15,0,0,0,20,15],
    ["Oud",0,10,0,0,25,15,0,0,0],
    ["Palmeira",0,0,0,0,0,0,20,10,20],
    ["Pretzel",0,0,15,0,10,0,0,0,25],
    ["Prince",0,20,0,0,0,0,10,20,0],
    ["Rena",0,10,0,0,20,0,20,0,0],
    ["Rooster",0,0,10,0,0,20,0,20,0],
    ["Samba",5,0,25,0,20,0,0,0,0],
    ["Schooner",0,0,0,25,15,0,10,0,0],
    ["Self_Control",0,0,5,5,0,0,0,0,5],
    ["Street_Shark",15,0,0,0,0,10,0,25,0],
    ["Taurus",20,0,25,0,0,5,0,0,0],
    ["Tsar",0,15,0,0,0,0,10,0,25],
    ["Tulip",0,0,0,20,20,0,10,0,0],
    ["Tune_In",10,15,0,0,25,0,0,0,0],
    ["Unstoppable",15,0,10,0,0,25,0,0,0],
    ["Vice",10,0,15,0,10,0,0,0,0],
    ["Warrior",10,0,0,0,0,5,5,0,0]
]

# Crie um gráfico direcionado
G = nx.DiGraph()

# Adicione nodos para os nomes na primeira coluna
for i in range(1, len(data)):
    G.add_node(data[i][0], color='blue')  # Stats são azuis

# Adicione nodos para os stats na primeira linha
for stat in data[0][1:]:
    G.add_node(stat, color='red')  # Stats são vermelhos

# Adicione as arestas com valores não nulos
for i in range(1, len(data)):
    for j in range(1, len(data[0])):
        if data[i][j] != 0:
            G.add_edge(data[i][0], data[0][j])

# Crie um layout circular
pos = nx.circular_layout(G)

# Obtenha as cores dos nodos
node_colors = [node[1]['color'] for node in G.nodes(data=True)]

# Desenhe os nodos com rótulos
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000)
labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_color='white')

# Desenhe as arestas com setas
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color='black', arrows=True)

# Exiba o gráfico
plt.axis('off')
plt.show()

