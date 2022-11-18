from collections import defaultdict
import sys
import time

#Param: Lista con todas las palabras del diccionario en orden
#Return: Lista con orden del alfabeto
def orden(lista):

    #Sacar todas las letras del alfabeto
    alfabeto = {}
    for palabra in lista:
        for letra in palabra:
            if letra not in alfabeto:
                alfabeto[letra] = 0

    #Creacion de un grafo vacio
    grafo = defaultdict(set)
    
    #Crea los arcos del grafo dependiendo de las relaciones
    i=0
    j=0
    while i<len(lista)-1:
        palabra1 = lista[i]
        palabra2 = lista[i+1]
        j=0
        while j<len(palabra1) and j<len(palabra2):
            letra1 = palabra1[j]
            letra2 = palabra2[j]
            if letra1 != letra2:
                if letra2 not in grafo[letra1]:
                    grafo[letra1].add(letra2)
                    alfabeto[letra2] += 1
                break
            j=j+1
        i=i+1
    
    #Crear una lista con todos los nodos sin relacion saliente
    vertices_sin_salida = []

    orden = ''

    #Llenar la lista de los nodos sin relacion saliente
    for vertice in alfabeto.keys():
        if alfabeto[vertice] == 0:
            vertices_sin_salida.append(vertice)

    #Se le añaden los nodos faltantes a la lista y se ordena de forma topologica el grafo
    while vertices_sin_salida != []:
        ultimo = vertices_sin_salida[-1]
        orden += ultimo
        vertices_sin_salida.remove(ultimo)
        for letra in grafo[ultimo]:
            alfabeto[letra] -= 1
            if alfabeto[letra] == 0:
                vertices_sin_salida.append(letra)

    #Se verifica que no existan ciclos en el grafo
    if len(orden) < len(alfabeto):
        return "ERROR"

    return orden

def ordenar_paginas(dict):

    paginas_ordenadas = sorted(dict.keys())
    ordenado = {}
    lista = []

    for pagina in paginas_ordenadas:
        ordenado[pagina] = dict[pagina]
    
    for pagina in ordenado:
        lista+=ordenado[pagina]

    return lista

def main():
    linea = sys.stdin.readline()
    total = int(linea)
    for i in range(0, total):
        linea = sys.stdin.readline()
        paginas_palabras = linea.split()
        diccionario = {}
        for j in range(0, int(paginas_palabras[0])):
            linea = sys.stdin.readline()
            lista = linea.split()
            pagina = lista[0]
            lista.remove(pagina)
            diccionario[pagina] = lista
        lista = ordenar_paginas(diccionario)
        print(orden(lista))

inicio = time.time()
main()
fin = time.time()
print("Time: "+ str(fin-inicio))