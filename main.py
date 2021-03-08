from random import randint

def llenar_matriz(n):#funcion, n sera el tamaño de la matriz
    matriz = []  #creamos la variable que se llame matriz , que sera un arreglo

    for r in range(n):#el primero ciclo for es para iterar las 
        fila = []
        
        #este ciclo for anidado ,que va a recorrer cada una de las columnas para la fila actual
        for c in range(n):#por cada c columna en el mismo rango, la cantidad de columnas que indique n
            fila.append(randint(1,100))#generar un entero aleatorio, 1 es el minimo y 100 es el maximo
        
        matriz.append(fila)       
    return matriz  #al final retornamos lo que hay en matriz
    
resultado = llenar_matriz(5)#una matriz de 5x5 cada fila tiene 5 elementos
print(resultado)