#Ejemplo básico: Recorrer una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)


#Ejemplo con range(): Contar números
for i in range(5):  # Va del 0 al 4
    print(i)


#Ejemplo práctico: Tabla de multiplicar 
num = int(input("Ingresa un número: "))
for i in range(1, 11): #genera los números del 1 al 10
    print(f"{num} x {i} = {num * i}")


#Registro de asistencia de empleados
empleados = ["Ana", "Luis", "Carlos", "Marta", "Elena"]

for empleado in empleados:
    print(f"{empleado}, ¿has llegado? (si/no)")
    respuesta = input().lower()  # Convertimos la respuesta a minúsculas

    if respuesta == "si":
        print(f"{empleado} está presente ✅\n")
    else:
        print(f"{empleado} está ausente ❌\n")


#Calculadora de Salarios 
Em = ["Ana","Luis","Marta"]

for Emp in Em:
  h = float(input("Ingrese las horas trabajadas por "+Emp+ ": "))
  p = float(input("Ingrese el pago por hora de "+Emp+ ": "))
  salario = h * p
  print(f"{Emp} ha ganado {salario:.2f} Euros") #:.2f en la impresión para mostrar dos decimales


