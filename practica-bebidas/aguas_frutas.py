#Programa que permite vender bebidas
#Solicita una opcion para elegir la bebida
#Preguntas la cantidad de bebida
#Muestra el total a pagar
print("Aguas de litro Uagro")
print("---Menu de bebidas---")
print("1.Agua de mango - $40")
print("2.Agua de jamaica - $45")
print("3.Agua de horchata - 35")

opcion = int(input("Elige una opcion del menu:"))
cantidad = int(input("cuantos litros quieres?"))

if opcion == 1:
    bebidas = 'agua de mango'
    precio = 40
elif opcion == 2:
    bebidas = 'agua de jamaica'
    precio = 45
elif opcion == 3:
    bebidas = 'agua de horchata'
    precio = 35
else:
    bebidas = 'No existe bebida'
    precio = 0
if precio > 0:
    total = precio * cantidad
    print(f"{cantidad} de {bebidas}")
    print(f"Total a pagar $:{total}")
else:
    print("No existe bebida")
    print("Holas wenas wenas")