Ejercicio: Una empresa quiere calcular el bono de productividad de sus empleados según la cantidad de proyectos completados en el mes.

📌 Reglas de bono:

Si un empleado completó 5 o más proyectos, recibe 100€ por cada uno. Si completó menos de 5, recibe 50€ por cada uno.

🔹 Tu tarea:

Pedir la cantidad de proyectos completados para cada empleado. Calcular y mostrar el bono correspondiente.

Empleado = ["Ana","Luis","Marta"]

for em in Empleado:
  Pro = int(input(f"Ingrese cantidad de prtoyectos completados por {em}:"))
  if Pro >=5:
    bono = Pro*100
    print(f"El bono de {em} es de {bono}")
  else:
    bono = Pro*50
    print(f"El bono de {em} es de {bono}")
