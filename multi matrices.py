import os
input("Presiona 'enter' para sumar las matrices ")
os.system("cls")
matriz_a = [[1, 2, 3],
            [6, 7, 8],
            [4, 5, 3]]

matriz_b = [[4, 5, 5],
            [9, 0, 3],
            [2, 3, 4]]

def producto_matrices(a, b):

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



producto = producto_matrices(matriz_a, matriz_b)
if producto:
  
    for fila in producto:
        for valor in fila:
          
            print(valor, end=" ")
        print("")
else:
    print("El número de columnas de A es distinto al número de filas de B")