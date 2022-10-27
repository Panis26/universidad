
graph1 = [
        [0,1,0,5],
        [1,0,4,5],
        [0,4,0,2],
        [5,5,2,0]
        ]
graph2 = [
        [0,6,1,5,0,0],
        [6,0,5,3,0,0],
        [1,5,0,5,6,4],
        [5,0,5,0,0,2],
        [0,3,6,0,0,6],
        [0,0,4,2,6,0]
        ]
graph3 = [
        [0,7,0,5,0,0,0],
        [7,0,8,9,7,0,0],
        [0,8,0,0,5,0,0],
        [5,9,0,0,15,6,0],
        [0,7,5,15,0,8,9],
        [0,0,0,6,8,0,11],
        [0,0,0,0,9,11,0]
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

def kruskal(graph):

    lenGraph = len(graph)
    visited = [False] * lenGraph

    menorCosto = []
    posibilidades = {}
    
    for i in range(lenGraph):
        for j in range(lenGraph):
            if graph[i][j] != 0:
                if (j,i) not in posibilidades:
                    posibilidades[i,j] = graph[i][j]

    allVisited = nodosVisited(visited)

    while(not allVisited):
        menor = min(posibilidades.values())
        nodoOrigenMin,nodoDestinoMin = get_key(posibilidades,menor)
        
        del posibilidades[nodoOrigenMin,nodoDestinoMin]
        menor = min(posibilidades.values())
        nodoOrigenMin,nodoDestinoMin = get_key(posibilidades,menor)

        menorCosto.append((nodoOrigenMin,nodoDestinoMin))
        del posibilidades[nodoOrigenMin,nodoDestinoMin]

        allVisited = nodosVisited(visited)

    return menorCosto

print(kruskal(graph1))



        