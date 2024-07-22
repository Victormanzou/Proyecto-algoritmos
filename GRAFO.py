import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.algorithms.simple_paths import all_simple_paths

vertices = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
aristas = [
    (1, 3), (1, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 4), (4, 5),
    (4, 6), (4, 7), (5, 6), (5, 7), (6, 7), (7, 6), (6, 4),
    (6, 8), (7, 9), (7, 8), (8, 9), (9, 8), (9, 10), (8, 10), (10, 11),
    (10, 12), (11, 13), (12, 14), (13, 15), (15, 17), (17, 19), (19, 21),
    (21, 23), (21, 22), (23, 25), (23, 24), (24, 25), (25, 24), (14, 15),
    (14, 16), (16, 19), (16, 18), (18, 21), (18, 20), (20, 23), (20, 22),
    (22, 24), (22, 25)
]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(aristas)

shortest_path_1_to_25 = shortest_path(G, source=1, target=25)

all_paths = list(all_simple_paths(G, source=1, target=25))
longest_path_1_to_25 = max(all_paths, key=len)

plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=15, font_weight="bold", edge_color="black")

path_edges = list(zip(shortest_path_1_to_25, shortest_path_1_to_25[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="OrangeRed", width=7)

path_edges_long = list(zip(longest_path_1_to_25, longest_path_1_to_25[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges_long, edge_color="LightSalmon", width=3.5, style="solid")

print("Camino corto:", shortest_path_1_to_25)
print("Camino largo:", longest_path_1_to_25)

plt.show()