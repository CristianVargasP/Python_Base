#Ejemplo: Monitoreo de inventario de productos

productos = {
    "Camisetas": 10,
    "Pantalones": 5,
    "Zapatos": 2,
    "Chaquetas": 0
}

# Definir el umbral mínimo de inventario
umbral_minimo = 3

while True:
    # Preguntar al usuario qué producto desea revisar
    producto = input("¿Qué producto deseas verificar (o 'salir' para terminar)? ").capitalize()

    if producto == 'Salir':
        print("Terminando el programa.")
        break  # Salimos del bucle si el usuario escribe 'salir'

    # Verificamos si el producto está en el inventario
    if producto in productos:
        stock = productos[producto]
        print(f"Stock de {producto}: {stock}")

        if stock < umbral_minimo:
            print(f"Alerta: El stock de {producto} está por debajo del umbral mínimo.")
        else:
            print(f"El stock de {producto} es suficiente.")
    else:
        print(f"El producto '{producto}' no se encuentra en el inventario.")



#Ejercicio: Sumar números hasta que el usuario decida detenerse

suma= 0

while True:
  Num=input("ingrese uno numeros( o 'fin' para terminar): ")

  if Num == 'fin':
    print(f"La suma es {suma}")
    break
  else:
    suma +=int(Num)
    print(f"La suma es {suma}")

#Ejercicio: Cajero Automático

Saldo = int(input("Ingrese su saldo inicial: "))
while True:
  retiro = int(input("Ingrese el monto a reitrar(0 para salir): "))
  if retiro == 0:
    print(f"Operacion finalizada. Saldo restante {Saldo}")
    break

  elif retiro <= Saldo:
    Saldo -= retiro
    print(f"Retiro exitoso. Saldo restante: {Saldo}")

  else:
    print("Error, Saldo insuficiente. Intente un monto menor")


#Ejercicio: Verificación de Contraseña Crea un programa que solicite al usuario una contraseña y la valide

Contraseña = "f123"
cont = 0
while True:
  contr = input("ingrese la contraseña: ").strip()#Elimina espacios accidentales
  if contr == Contraseña:
    print("Contraseña correcta")
    break
  else:
    cont += 1
    if cont == 3:
      print("Acesso bloqueado")
      break
    else:
      print("Contraseña incorrecta")


#Ejercicio: Control de inventario 

Inventario = 100

while True:
  Vendido = int(input("Ingrese la cantidad vendida: "))
  if Vendido < Inventario:
    Inventario -= Vendido
    print(f"Venta realizada. Productos restantes: {Inventario}")
  elif Vendido > Inventario:
    print(f"Error: No hay suficientes productos en el inventarios. Intente un numero menor. Productos restantes: {Inventario}")
  else:
    Inventario -= Vendido
    print("Venta realizada. Invetario agotado")
    break

