#ejemplo y uso de try except
#num=int(input("Ingrese un numero")) #NUMERO ENTERO INT
#QUE PASA SI INGRESAS UNA PALABRA EN VEZ DE UN NUMERO? COMO MANEjAR EL ERROR
# while True: #runtime: tiempo de ejecion, tiempo que se ejecuta el programa "while"
#     try:
#         num=int(input("Ingrese un numero "))
#         break 
#     except:
#         print("solo numeros enteros ") 
#     #asi evitamos que tire error en caso de que el usuario ingrese un dato o formato incorrecto
#     #validar y manejar el error de esta forma

#sacar promedio
# print("ingrese 3 notas")
# total=0

#         for i in range (3):
#             n=float(input(f"ingrese la nota {i+1}: "))
#             total+=n
# prom=total/3
# print=(f"el promedio es {prom}") ###corrigeeee##

#Mostrar el error:::::::::::. Hacer::::::::

#:::::::::::::::::::::::::::EJERCICIO GIT PROFE:::::::::::::::::::::::

op=0
total=0
while op!=4:
     print("1.- PC $500.000")
     print("2.- LGTV 55 pulgadas $450.000")
     print("3.- Microondas Mademsa $100.000")
     print("4.- Salir")
     print("Seleccione una opcion")
     op=int(input())
     match op:
         case 1:
             print("El total a pagar es ",500000*1.19 )
             total+=500000*1.19
         case 2:
             print("El total a pagar es ",450000*1.19 )
             total+=450000*1.19
         case 3:
             print("El total a pagar es ",100000*1.19 )
             total+=100000*1.19
         case 4:
             print("Saliendo")
             print("El total a pagar es", total)
         case _:
             print("Opción inválida")