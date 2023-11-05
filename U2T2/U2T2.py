# Bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

# Criar um objeto de grafo
G = nx.Graph()
fig, ax = plt.subplots(figsize=(7,7))

# Criar os conjuntos de nós
node_left = set()
node_right = set()

start_time = time.time()

# Leitura do arquivo de texto e adicionar os nós aos conjuntos
with open('CA-CondMat.txt', 'r') as file:
  #Trocar o nome do arquivo para o que desejar ver o gráfico
    for line in file:
        n1, n2 = map(int, line.strip().split())

        # Separar dados nos conjuntos correspondentes
        node_left.add(n1)
        node_right.add(n2)
        # Adicionar arestas
        G.add_edge(n1, n2)

# Adicionar nós aos conjuntos correspondentes
G.add_nodes_from(node_left, bipartite=0)
G.add_nodes_from(node_right, bipartite=1)

# Calcular coeficiente de assortatividade
assort = nx.degree_assortativity_coefficient(G)

# Contar nós e arestas
nodes_num = G.number_of_nodes()
edge_num = G.number_of_edges()

# Contar o número de componentes conectados
connected_components = nx.number_connected_components(G)

# Contar o tamanho do componente gigante
connected_components_list = list(nx.connected_components(G))
gcc = max(connected_components_list, key=len)
size_gcc = len(gcc)

# Calcular média de clustering
media_cluster = nx.average_clustering(G)
# Calcular coeficiente de clustering
cluster = nx.clustering(G)

# Conectividade média dos graus
avg_degree = nx.average_degree_connectivity(G)

degrees, avg_connect = zip(*avg_degree.items())

# Gráfico de dispersão
plt.scatter(degrees, avg_connect, alpha=0.5, label='Scatter Plot')

b, a = np.polyfit(degrees, avg_connect, deg=1)
xseq = np.linspace(min(degrees), max(degrees), num=300)
ax.plot(xseq, a + b * xseq, color='k', lw=2.5)

# Adicionando linha de assortatividade
plt.axhline(assort, color='green', linestyle='--', label='Assortativity')

end_time = time.time()
execution_time = end_time - start_time

# Legendas
plt.xlabel('Node Degree')
plt.ylabel('Average Neighbor Degree (AND)')
plt.legend()

plt.title('CA-CondMat')
#Trocar o nome para o que desejar ver o nome do título

# Print das informações procuradas
# print(f'Coef. de clustering (AVG): {cluster:}')
print(f'Tempo de execução (s): {execution_time:.2f} s')
print(f'Coef. de Assortatividade: {assort:.4f}')
print(f'Número de nós: {nodes_num}')
print(f'Número de arestas: {edge_num}')
print(f'Qtd de Componentes Conectados: (QCC): {connected_components}')
print(f'Tamanho do Componente Gigante: (GCC): {size_gcc}')
print(f'Média de clustering: {media_cluster:.4f}')

plt.show()
