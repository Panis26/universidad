#Cristian Armando Sánchez Ocampo

import random

#Grafos ejemplo con estructura de lista de adyacencia
#La posición de la lista representa el nodo y Lista[i] representa los nodos adyacentes a este nodo
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

#Revisa en una lista de booleanos si todos los nodos fueron visitados
def nodosVisited(visited):
    for i in range(len(visited)):
        if visited[i] == False:
            return False
    return True

#Obtiene la llave de un diccionario a partir de su valor
def get_key(dicc,val):
    for key, value in dicc.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def prim(graph):
    lenGraph = len(graph)
    visited = [False] * lenGraph
    menorCosto = []
    
    #Inicia en un nodo aleatorio
    nodoInicial = random.randint(0,lenGraph-1)

    #Aqui se verifica si todos los nodos fueron visitados
    allVisited = nodosVisited(visited)

    nodo = nodoInicial
    adyacentes = graph[nodoInicial] 
    
    posibilidades = {}

    #Se recorre la lista de adyacencia del nodo inicial mientras no se hayan visitado todos los nodos
    while(not allVisited):
        for key in adyacentes:
            if visited[key] == False:
                #Se guarda en un diccionario las posibilidades de adyacencia con su costo
                posibilidades[nodo,key] = adyacentes[key]

            #Se elimina la arista para no ser guardad 2 veces
            if (key,nodo) in posibilidades:
                    del posibilidades[(key,nodo)]

        visited[nodo] = True

        #Se obtiene el nodo con menor costo
        if len(posibilidades) > 0:
            menorArista = min(posibilidades.values())

            #Se camia el nodo inicial con el siguiente con el camino más corto
            nodoOrigen,nodoDestino = get_key(posibilidades,menorArista)
            del posibilidades[nodoOrigen,nodoDestino]
            
            #Se guarda la arista con menor costo
            menorCosto.append((nodoOrigen,nodoDestino))

            nodo = nodoDestino
            adyacentes = graph[nodo]
        allVisited = nodosVisited(visited)           
        
    return menorCosto

print(prim(graph1))
print(prim(graph2))
print(prim(graph3))

