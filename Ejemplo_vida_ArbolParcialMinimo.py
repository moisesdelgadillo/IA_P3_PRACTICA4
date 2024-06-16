# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:40:52 2024

@author: moise
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim_mst(graph, start_node):
    mst = nx.Graph()  # Grafo para el MST resultante
    visited = set()  # Conjunto de nodos visitados
    edges = []  # Cola de prioridad para las aristas (peso, nodo_origen, nodo_destino)

    # Añadir las aristas del nodo inicial a la cola de prioridad
    def add_edges(node):
        visited.add(node)  # Marcar el nodo como visitado
        for neighbor in graph[node]:
            if neighbor not in visited:
                weight = graph[node][neighbor]['weight']  # Obtener el peso de la arista
                heapq.heappush(edges, (weight, node, neighbor))  # Añadir arista a la cola
        # print(f"Nodo visitado: {node}, aristas añadidas: {graph[node]}")

    add_edges(start_node)  # Empezar con el nodo inicial

    while edges:
        weight, node1, node2 = heapq.heappop(edges)  # Obtener la arista de menor peso
        if node2 not in visited:
            mst.add_edge(node1, node2, weight=weight)  # Añadir arista al MST
            # print(f"Arista añadida al MST: ({node1}, {node2}), peso: {weight}")
            add_edges(node2)  # Añadir las aristas del nuevo nodo al MST

    return mst

# Crear un grafo de ejemplo (tiendas y costos de viaje entre ellas)
G = nx.Graph()
G.add_edge('Casa', 'Tienda_A', weight=5)
G.add_edge('Tienda_A', 'Tienda_B', weight=3)
G.add_edge('Tienda_B', 'Tienda_D', weight=4)
G.add_edge('Tienda_B', 'Tienda_C', weight=1)
G.add_edge('Tienda_C', 'Tienda_E', weight=2)
G.add_edge('Tienda_D', 'Tienda_E', weight=4)
G.add_edge('Tienda_E', 'Tienda_F', weight=1)

# Aplicar el algoritmo de Prim
mst = prim_mst(G, 'Casa')

# Dibujar el grafo original
plt.figure(figsize=(12, 6))

plt.subplot(121)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo Original (Rutas entre tiendas)')

# Dibujar el MST
plt.subplot(122)
pos = nx.spring_layout(mst)
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=16)
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
plt.title('Ruta Más Eficiente (MST)')

plt.show()

# Mostrar el progreso en la consola
print("Proceso del algoritmo de Prim completado.")
print("Nodos y aristas en el MST resultante:")
for edge in mst.edges(data=True):
    print(edge)
