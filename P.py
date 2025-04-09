Empleado = ["Ana","Luis","Marta"]

for em in Empleado:
  Pro = int(input(f"Ingrese cantidad de prtoyectos completados por {em}:"))
  if Pro >=5:
    bono = Pro*100
    print(f"El bono de {em} es de {bono}")
  else:
    bono = Pro*50
    print(f"El bono de {em} es de {bono}")
