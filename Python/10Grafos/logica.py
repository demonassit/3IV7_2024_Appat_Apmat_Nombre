import heapq

def dijkastra(grafo, inicio):
    #primero debo de conocer las distancias
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
    distancias

def kruskal(aristas, nodos):
    aristas = sorted(aristas, key=lambda x: x[2]) #ordenando por el peso
    padre = {nodo : nodo for nodo in nodos}

    def encontrar(nodo):
        if padre[nodo] != nodo:
            padre[nodo] = encontrar(padre[nodo])
        return padre[nodo]

    mst = []

    for u, v, peso in aristas:
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)
        if raiz_u != raiz_v:
            mst.append((u, v, peso))
            padre[raiz_u] = raiz_v
    return mst