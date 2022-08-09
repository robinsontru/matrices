matriz_a = []
lista=[]

matriz_b = [[2,0,0],
            [0,2,0],
            [0,0,2],      ]
def multiplicaciones(a,b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

producto = multiplicaciones(matriz_a, matriz_b)
for i in range(0,4) :
    lista=[input("dame un numero") for j in range(3)]
    matriz_a.append(lista)
    print(matriz_a)
if producto:
  
    for fila in producto:
        for valor in fila:
          
            print(valor, end=" ")
        print("")
else:
    print("El número de columnas de A es distinto al número de filas de B")
####


