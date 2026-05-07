import random
# n1 = int(input("ingrse el valor de limite inferior "))
# n2 = int(input("ingrese el valor del limite superior"))
# #VALIDAR QUE EL LIMITE SUPERIOR SEA MAYOR QUE EL LIMITE INFERIOR
# num = random.randint(n1,n2)
# while n1>=n2
#     print ("error, el limite superior debe ser mayor al limite inferior")
#     n2 = int(input("ingrese el valor del limite superior"))
# num=random.radint(n1,n2)
# print(num)

#Ejercicio tipo prueba
#Resolucion diego:::::: y profe
# lata=0
# plancha=0
# peces=random.randint(10,20)
# print(f"la cantidad de peces capturados son: {peces} peces")
# time.sleep
# for i in range(peces):
#     peso=random.radint(300,3000)
#     if peso <=800:
#         lata+= 1
#     if peso >= 801 and peso <=3000:
#         plancha += 1
#     else:
#         print("peso invalido")
# time.sleep(2)
# print(f"El total de peces en lata son {lata}")
# time.sleep(2)
# print(f"el total de peces en plancha son {plancha}")

# EJERCICIO 2: FABRICA DE ENLOTADOS
# PRUEBA EJEMPLO: DISTINTAS CONDICIONALIDADES

#sodio rango 1 a 100
#peso debe ser positivo
#--------------------------------------------------
#consideracion: venta nacional o internacional *criterio?*
#si el peso del producto: -500g=lata normal
#501 hasta 1500 g: lata mediana
#mas de 1501: lata grande
#--------------------------------------------------------------------------------
#si NA: >5%: lata queda igual
#si NA: 5% Y 8%: LATA ESPECIAL
#si NA: 9% o mas: lata acorazada
# las latas internaionales, se les debe pegar un stiker de validacion sanitaria
#---------------------------------------------------------------------------
#pedir 3 valores: peso,%, nacional o internacional
peso=(int(input("ingrese el peso del producto: ")))

sodio=(int(input("ingrese el porcentaje de sodio")))

mercado=(int(input("ingrese el mercado del producto: 1.- nacional, 2.- interacional")))

if peso<500:
    lata="lata normal"
elif 501<peso<1500:
     lata="lata mediana"
else:
    lata="lata grande"

if sodio<5:
    sod=""
elif 5<=sodio<=8:
    sod="lata especial"
else:
    sod="acorazada"

if mercado==1:
    sticker="" #nacional
else:
    sticker="con sicker sanitario"

print(f"{lata} {sod} {sticker}")