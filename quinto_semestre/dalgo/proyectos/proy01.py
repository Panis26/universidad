def contarTodo (sec,subsec):
    cont = 0
    lista1 = []
    lista2 = []
    for i in range(0,len(sec)):
        if (sec[i] == subsec[1]):
            lista1.append(i)
        if (sec[i] == subsec[0]):
            lista2.append(i)
    
    for j in lista1:
        for k in lista2:
            if (j>k):
                cont+=1
            else:
                break
    return cont 

def contar (sec, subsec, der):
    cont = 0
    if (der):
        for i in range(1,len(sec)):
            if (sec[i] == subsec[1]):
                cont = cont + 1
    else:
        for i in range(0,len(sec)-1):
            if (sec[i] == subsec[0]):
                cont = cont + 1
    return cont

def funcion (sec, subsec, m, i):
    if (i == len(sec)):
        memoria[sec] = contarTodo(sec, subsec)
    if (m==0):
        return memoria[sec]
    elif(i==0):
        return memoria[sec]
    else:
        l = list(subsec)
        l1 = list(sec)
        cad1 = l1.copy()
        cad2 = l1.copy()
        cad1[i-1] = l[0]
        cad2[i-1] = l[1]
        cad1 = "".join(cad1)
        cad2 = "".join(cad2)
        if (l1[i-1] == l[0] and l[0] == l[1]):
            return funcion(sec, subsec, m, i-1) #No se cambia nada
        elif (l1[i-1] == l[0]):
            memoria[cad2] = memoria[sec] + contar(cad2[:i], subsec, False)
            return max(funcion(sec, subsec, m, i-1), funcion(cad2, subsec, m-1, i-1)) #Se cambia el segundo caracter
        elif (l1[i-1] == l[1]):
            memoria[cad1] = memoria[sec] + contar(cad1[i-1:], subsec, True)
            return max(funcion(sec, subsec, m, i-1), funcion(cad1, subsec, m-1, i-1)) #Se cambia el primer caracter
        else:
            memoria[cad1] = memoria[sec] + contar(cad1[i-1:], subsec, True)
            memoria[cad2] = memoria[sec] + contar(cad2[:i], subsec, False)
            return max(funcion(sec, subsec, m, i-1), funcion(cad1, subsec, m-1, i-1), funcion(cad2, subsec, m-1, i-1)) #Se cambian ambos caracteres
    
if _name=="main_":
    sec = "aaaaaa"
    subsec = "aa"
    memoria = {}
    print(funcion(sec,subsec,20,len(sec)))
#Simetria
#El priemero 2 de la subsec obvio mal
#El primero 1 de la subsec bien

#El ultimo 1 de la subsec puede bien