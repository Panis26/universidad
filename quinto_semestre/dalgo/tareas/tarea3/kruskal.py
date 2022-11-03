#Cristian Armando Sánchez Ocampo
import random

#Grafos ejemplo con estructura de matriz de adyacencia
#La posición de la lista representa el nodo, Lista[i] representa los nodos adyacentes a este nodo,  Lista[i][j] representa el costo de ir del nodo i al nodo j
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

def kruskal(graph):

    lenGraph = len(graph)
    visited = [False] * lenGraph

    menorCosto = []
    posibilidades = {}
    #Recorre la matriz de adyacencia en busca de los costos de los arcos
    for i in range(lenGraph):
        for j in range(lenGraph):
            if graph[i][j] != 0:
                if (j,i) not in posibilidades:
                    #Los costos de los arcos se guardan en un diccionario con sus repectivos nodos
                    posibilidades[i,j] = graph[i][j]

    #Verifica si todos los nodos fueron visitados
    allVisited = nodosVisited(visited)

    while(len(posibilidades)>0 ):
        #Obtiene el costo minimo entre todos los arcos del grafo
        menor = min(posibilidades.values())
        nodoOrigenMin,nodoDestinoMin = get_key(posibilidades,menor)

        #Elimina ese arco del diccionario
        del posibilidades[nodoOrigenMin,nodoDestinoMin]

        #Si el nodo origen y el nodo destino no han sido visitados, se agrega el arco al arbol de menor costo, (Esto para que no exista ciclo)
        if len(posibilidades) > 0:
            menor = min(posibilidades.values())
            nodoOrigenMin,nodoDestinoMin = get_key(posibilidades,menor)

            menorCosto.append((nodoOrigenMin,nodoDestinoMin))
            del posibilidades[nodoOrigenMin,nodoDestinoMin]

            allVisited = nodosVisited(visited)

    return menorCosto

print(kruskal(graph1))
