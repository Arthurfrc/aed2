import Parts
import Classes
import Functions
import networkx as nx
import matplotlib.pyplot as plt

setups = []
setup_filter = []
setup_teamscore = []

Functions.Setup_Cards(setups)

#Plot do histograma

for y in range(len(setups)):
    setup_teamscore.append(setups[y].teamscore)

plt.hist(setup_teamscore)
plt.show()

Functions.Top_100(setups, setup_filter)
print(len(setup_filter))

