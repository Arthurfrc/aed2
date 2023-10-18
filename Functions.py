import Classes
import Parts
import networkx as nx


#G = nx.DiGraph()

# Criando um setup
def Setup_Cards(setups=[], t=0):
    for b in range(8):
        for g in range(8):
            for r in range(8):
                for f in range(8):
                    for s in range(8):
                        for e in range(8):
                            setup_temp = Classes.Setup(Parts.Brakes[b], Parts.Gearbox[g], 
                                                       Parts.Rear_wing[r], Parts.Front_wing[f], 
                                                       Parts.Suspension[s], Parts.Engine[e], t)
                            t += 1
                            setups.append(setup_temp)




#plt.savefig("histograma.png")


def Top_100(setups = [], setup_filter = []):
    # Ordenando o array de setups
    setups.sort(key=lambda temp: temp.teamscore, reverse=True)
    # Filtrando os melhores N arrays
    for j in range(100):
       if j < len(setups):
            setup_filter.append(setups[j])
            #print(setup_filter[j].teamscore)

#print(len(setup_filter))

# Essa função recebe um grafo G e coloca nodes com cada parte possível
def add_nodes_from_parts(G):
    part_lists = [Parts.Brakes, Parts.Gearbox, Parts.Front_wing, Parts.Rear_wing, Parts.Engine, 
                  Parts.Suspension]
    
    for part_list in part_lists:
        for part in part_list:
            G.add_node(part.name, part=True)


# Função que cria os nodes do grafo baseado no nome dos setups
def add_nodes_from_setups(G, setup_filter):
    for i in range(len(setup_filter)):
        G.add_node(setup_filter[i].name, part=False)

# Função que cria as arestas do grafo
def add_edges(G, setup_filter=[]):
    part_mapping = {
        "Brakes": Parts.Brakes,
        "Gearbox": Parts.Gearbox,
        "Suspension": Parts.Suspension,
        "Rear_wing": Parts.Rear_wing,
        "Front_wing": Parts.Front_wing,
        "Engine": Parts.Engine,
    }

    for part_name, part_list in part_mapping.items():
        for i in range(len(part_list)):
            for j in range(len(setup_filter)):
                setup_part = getattr(setup_filter[j], part_name.lower())
                if setup_part.name == part_list[i].name:
                    G.add_edge(part_list[i].name, setup_filter[j].n)






