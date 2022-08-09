import os
input("Presiona 'enter' para sumar las matrices ")
os.system("cls")
m1=[[1, 2, 3], [4, 5, 6]]
m2=[[1, 2, 3], [4, 5, 6]]
m3=[[0, 0, 0], [0, 0, 0]]
for i in range (0,2):
    for l  in range (0,3):    
     for i in range (0,2):
       for l  in range (0,3):       
         for i in range (0,2):
           for l  in range (0,3):
            m3[i][l]=m1[i][l]+m2[i][l]
print(m1)
print(m2)
print(m3)

