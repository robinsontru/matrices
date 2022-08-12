
import os 
import csv
def cuenta_de_banco (nombre_cuenta):
    Ncuenta=int(input("cracion de nueva cuenta "))
    with open (nombre_cuenta,"a",newline="")as archivo_csv:
        write=csv.writer(archivo_csv,delimiter=",")
        for i in range (Ncuenta):
            os.system("cls")
            nombre=input("nombre de usuario")
            id=input("ingrese un id")
            consignar_corrinte=input("consignar en cuenta corriente")
            write.writerows([nombre,id,consignar_corrinte])
             # consignar_cuenta_de_ahorro=input("consignar en una cuenta de ahorro")
            #invertir_cdt=input("invertir en un CDT")
def recupar_cuenta(nombre_cuenta):
     os.system("cls")
     print("cuentas")
     with open (nombre_cuenta,"r",newline="")as archivo_csv:
        reader=csv.reader(archivo_csv)
        for linea in reader:
            print(f"nombre:{linea[0]}")
            print(f"id{linea[1]}")
            print(f"corriente{linea[2]}")
            print("~"*50)
def main():
    archivo="cuentas.csv"
    cuenta_de_banco(archivo)
    recupar_cuenta(archivo)
if  __name__=="__main__":
    main()
