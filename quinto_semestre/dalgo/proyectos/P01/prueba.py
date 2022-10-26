import sys
import time

def contar(a, b):
    m = len(a)
    n = len(b)
 
    lookup = [[0] * (n + 1) for i in range(m + 1)]
 
    for i in range(n+1):
        lookup[0][i] = 0
 
    for i in range(m + 1):
        lookup[i][0] = 1
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
            else:
                lookup[i][j] = lookup[i - 1][j]
 
    return lookup[m][n]

def funcion (sec, subsec, m):
    movimientos = m
    pos = 0
    listSub = list(subsec)
    listSec = list(sec)
    ultimo = ""
    while pos < len(listSec)//2 and movimientos > 0:
        if movimientos == 1:
            if listSec[pos] in listSub and listSec[-pos-1] in listSub:
                pos+=1
            if pos < len(listSec)//4 and listSec[-pos-1] not in listSub:
                listSec[-pos-1] = listSub[1]
                movimientos -= 1
                pos+=1
            else:
                cpy1 = listSec.copy()
                cpy2 = listSec.copy()
                cpy1[pos] = listSub[0]
                cpy2[-pos-1] = listSub[1]
                cpy1 = "".join(cpy1)
                cpy2 = "".join(cpy2)
                if contar(cpy1, subsec) < contar(cpy2, subsec):
                    listSec = list(cpy2)
                else:
                    listSec = list(cpy1)
                movimientos -= 1

        elif (len(listSec)%2 == 0):
            if listSec[pos] != listSub[0] and movimientos > 0:
                listSec[pos] = listSub[0]
                movimientos -= 1

            if listSec[-pos-1] != listSub[1] and movimientos > 0:
                listSec[-pos-1] = listSub[1]
                movimientos -= 1
            pos+=1
        else:
            if listSec[-pos-1] != listSub[1] and movimientos > 0:
                ultimo = listSub[1]
                listSec.pop(-pos-1)
                movimientos -= 1
            else: 
                if movimientos > 0:
                    ultimo = listSub[1]
                    listSec.pop(-pos-1)

    mejorCombinacion = "".join(listSec)+ultimo
    ocurrencias = contar(mejorCombinacion,subsec)

    return ocurrencias

def main():
    linea = sys.stdin.readline()
    total = int(linea)
    linea = sys.stdin.readline()
    start_time = time.time()
    for i in range(0, total):
        cadenas = [str(cadena) for cadena in linea.split()]
        rta = funcion(cadenas[0], cadenas[1], int(cadenas[2]))
        print(str(rta))
        linea = sys.stdin.readline()
    print ("tiempo de ejecucion: ", time.time() - start_time)
main()
