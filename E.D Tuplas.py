# Ejercicio: Registro de Empleados en una Empresa

'''
1️⃣ Define una tupla para cada empleado con la siguiente información:

ID, Nombre, Cargo, Departamento, Salario
'''

Empleado_1 = (1001, "Felipe Vargas", "Desarrollador", "IT", 4000)
Empleado_2 = (1002, "Marina Perez", "Diseñadora", "Diseño", 3500)
Empleado_3 = (1003, "Andrey Vargas", "Contador", "Administrativa", 3000)

#2️⃣ Crea una lista de empleados para manejar varios registros.

Empleados = [Empleado_1, Empleado_2, Empleado_3]

#3️⃣ Muestra la información de cada empleado recorriendo la lista.
#Método: Bucle for con desempaquetado

for id_emp, nombre, cargo, departamento, salario in Empleados:
  print(f"ID: {id_emp}, Nombre: {nombre}, Cargo: {cargo}, Departamento: {departamento}, Salario: {salario}")


#4️⃣ Busca un empleado por su ID y muestra su información.
#Método: for con condición if

id_buscar = int(input("ingrese el id del empleado: "))

for emp in Empleados:
  if emp[0] == id_buscar:
    print(f"Empleado encontrado: {emp}")
    break
  else:
    print("Empleado no encontrado")

#5️⃣ Calcula el salario promedio de los empleados.
#Método: sum() y len()

total_salario = sum(emp[4] for emp in Empleados)

promedio_salario = total_salario / len(Empleados)
print(f"Salario promedio: {promedio_salario}")

#6️⃣ Verifica si hay un empleado con el cargo "IT".
Método: any()

Existe_cargo = any(emp[3]== "IT" for emp in Empleados)
print("¿Hay generente IT? ", Existe_cargo)
