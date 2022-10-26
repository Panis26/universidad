import sys
n, k = map(int, [200,20])
s = "hbadbbhfcafhcecgfcecbbaagbegbahcdacgcfbefafhbhcehffhfbfahfgcghhhefhcadgeghdagbadhgabfgchgbgebgdffbhebhgccgefhgadchghhfbhdeeahagghgegbebfbabedefdgdbbcbagfdebbdddfddacfefabbhceahhfhebecbbfegbahfgaghdhca"
t = "de"
 
dp = [[[-n * n] * (n + 1) for i in range(k + 1)] for i in range(n + 1)]
 
dp[0][0][0] = 0
for i in range(n):
	for j in range(k + 1):
		for l in range(n + 1):
			x = 1 if s[i] == t[0] else 0
			if l + x <= n:
				dp[i + 1][j][l + x] = max(dp[i + 1][j][l + x], dp[i][j][l] + (l if s[i] == t[1] else 0))
			
			if j < k and l < n:
				dp[i + 1][j + 1][l + 1] = max(dp[i + 1][j + 1][l + 1], dp[i][j][l] + (l if t[0] == t[1] else 0))
			
			if j < k:
				dp[i + 1][j + 1][l] = max(dp[i + 1][j + 1][l], dp[i][j][l] + l)
			
print(max(dp[n][k]))

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