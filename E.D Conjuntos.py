"" 
Ejercicio: Gestión de Alumnos en un Curso Imagina que tienes dos conjuntos de estudiantes en un curso:

Grupo A: Estudiantes que aprobaron el examen teórico.
Grupo B: Estudiantes que aprobaron el examen práctico.
"" 

#1.Crea dos conjuntos, grupo_teorico y grupo_practico, con nombres de estudiantes.

Teorico={"Felipe","Cristian","Nicolas","Marina"}
Practico={"Jose","Ana","Marina","Felipe"}

#2.#Muestra los estudiantes que aprobaron ambos exámenes (intersección).

Aprobo_ambas = Teorico.intersection(Practico)
print("Estudiantes que aprobaron ambos examenes",Aprobo_ambas)

#3.#Muestra los estudiantes que solo aprobaron uno de los dos exámenes.

Un_Examen = Teorico.symmetric_difference(Practico)
print("Estudiantes que aprobaron solo un de los examenes ",Un_Examen)

#4.#Muestra si algún estudiante aprobó solo el teórico pero no el práctico.

Solo_teorico = Teorico.difference(Practico)
if Solo_teorico:
  print("Estudiantes que aprobaron solo teorico: ",Solo_teorico)
else:
  print("No hay estudiantes que aprobaron solo el teorico")


#5.#Agrega un nuevo estudiante al grupo teórico y elimina a otro del grupo práctico.

Teorico.add("Tom") # Agregar un estudiante
Practico.discard("Felipe")# Eliminar un estudiante sin error si no existe

#6.# Muestra los conjuntos actualizados.

print("Conjunto de estudiantes examen teorico: ", Teorico)
print("Conjunto de estudiantes examen Practico: ", Practico)
