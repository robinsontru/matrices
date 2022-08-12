suma=0
asterisco="*"
#n1=int(input("ingrese un valor"))
opcion = 0
while True:
    print("""
    Dime, ¿cual es tu calificacion?
    1)A
    2)B
    3)C
    4)D
    5)E
    6)Terminar calificacion 
    """)
    opcion = int(input("Elige una opción: "))
    if opcion == 1:          
        print("")       
        print("la opcion A=1",)         
        for i in range (1,2):
         print ("A",asterisco*i)
         

    elif opcion == 2:
        print("")
        print("la opcion B=2")
        for i in range (1,3):
         print ("B",asterisco*i)
    elif opcion == 3:
        print("")
        print("la opcion C=3")
        for i in range (1,4):
         print ("C",asterisco*i)


    elif opcion == 4:
        print("")
        print("la opcion D=4")
        for i in range (1,5):
         print ("D",asterisco*i)
    elif opcion == 5:
        print("")
        print("la opcion E=5")
        for i in range (1,6):
         print ("E",asterisco*i)
    elif opcion == 6:
        print("")
        print("FIN")
        break


