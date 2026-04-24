from networkx import spring_layout
from numpy import asarray

# Helper function
def base_data(G,fob_scale,seed):
    """Função de utilidade"""
    
    # escalona FOB
    fob = []
    for e in G.edges():
        fob.append(G[e[0]][e[1]]['FOB'])
    fob = asarray(fob)/fob_scale # escala em USD

    # cria mapa de cores para arestas
    ne = G.number_of_edges()
    edge_colors = range(2,ne+2)

    # controle de randomização das coordenadas dos vértices/nós 
    coords = spring_layout(G,seed=seed) # layout

    return fob, edge_colors, coords