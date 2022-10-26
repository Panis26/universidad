import random

graph1 = [
        {1:1,3:5},
        {0:1,2:4,3:5},
        {1:4,3:2},
        {0:5,1:5,2:2}
        ]
graph2 = [
        {1:6,2:1,3:5},
        {0:6,2:5,4:3},
        {0:1,1:5,3:5,4:6,5:4},
        {0:5,2:5,5:2},
        {1:3,2:6,5:6},
        {2:4,3:2,4:6}
        ]
graph3 = [
        {1:7,3:5},
        {0:7,2:8,3:9,4:7},
        {1:8,4:5},
        {0:5,1:9,4:15,5:6},
        {1:7,2:5,3:15,5:8,6:9},
        {3:6,4:8,6:11},
        {4:9,5:11}
        ]

def nodosVisited(visited):
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

def get_key(dicc,val):
    for key, value in dicc.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def prim(graph):
    lenGraph = len(graph)
    visited = [False] * lenGraph
    menorCosto = []

    nodoInicial = random.randint(0,lenGraph-1)

    allVisited = nodosVisited(visited)

    nodo = nodoInicial
    adyacentes = graph[nodoInicial] 
    
    posibilidades = {}

    while(not allVisited):
        for key in adyacentes:
            if visited[key] == False:
                posibilidades[nodo,key] = adyacentes[key]

            if (key,nodo) in posibilidades:
                    del posibilidades[(key,nodo)]

        visited[nodo] = True
        if len(posibilidades) > 0:
            menorArista = min(posibilidades.values())
            nodoOrigen,nodoDestino = get_key(posibilidades,menorArista)
            del posibilidades[nodoOrigen,nodoDestino]
            menorCosto.append((nodoOrigen,nodoDestino))

            nodo = nodoDestino
            adyacentes = graph[nodo]
        
        allVisited = nodosVisited(visited)           
        
    return menorCosto

print(prim(graph1))
print(prim(graph2))
print(prim(graph3))

