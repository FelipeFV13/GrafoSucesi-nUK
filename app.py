import networkx as nx
import matplotlib.pyplot as plt

def agregar_arista(G, u, v, w, di = True):
    G.add_edge(u,v,weight=w)


if __name__ == '__main__':

    G = nx.DiGraph()

    #agregar par de nodos/arista
    agregar_arista(G,"King Charles III","William",1)
    agregar_arista(G,"William", "George", 2 )
    agregar_arista(G, "William", "Charlotte", 3)
    agregar_arista(G, "William", "Louis", 4)

    agregar_arista(G, "King Charles III", "Harry", 5)
    agregar_arista(G, "Harry", "Archie", 6)
    agregar_arista(G, "Harry", "Lilibet", 7)

    pos = {
        "King Charles III": (0.5, 1.0),
        "William": (0.3, 0.6),
        "Harry": (0.7, 0.6),
        "George": (0.2, 0.3),
        "Charlotte": (0.32, 0.3),
        "Louis": (0.45, 0.3),
        "Archie": (0.6, 0.3),
        "Lilibet": (0.8, 0.3)
    }
    nx.draw_networkx(G,pos, node_size=3000, font_size=8, node_color="lightgrey")
    lables = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=lables)
    plt.title("Sucesion Trono UK")
    plt.show()




