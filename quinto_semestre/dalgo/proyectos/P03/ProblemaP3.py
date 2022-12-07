import sys
import time
 
def funcion(m, k):
    pos = 0
    res = []
    dp = []
    temp = []
    for i in range(m+1):
        res.append(0)
    for i in range(m+2):
        dp.append(0)
        temp.append(0)
    dp[0] = 1
    while pos + k <= m:
        for i in range(k):
            n = pos + i
            actual = dp[n]
            n = n + k
            while n <= m:
                temp[n] = actual
                res[n] = res[n] + actual
                actual = actual + dp[n]
                n = n + k
        temp2 = temp
        temp = dp
        dp = temp2
        pos = pos + k
        k = k + 1

    for i in range(len(res)):
        res[i] %= 998244353

    return res[-1]

def main():
    linea = sys.stdin.readline()
    total = int(linea)
    linea = sys.stdin.readline()
    for i in range(0, total):
        cadenas = [str(cadena) for cadena in linea.split()]
        rta = funcion(int(cadenas[0]), int(cadenas[1]))
        print(str(rta))
        linea = sys.stdin.readline()	
	
inicio = time.time()
main()
fin = time.time()
print("Time: "+ str(fin-inicio) + 'ms')