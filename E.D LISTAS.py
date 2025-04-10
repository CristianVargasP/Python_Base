'''
Ejercicio: Gestión de Notas de Estudiantes Imagina que estás desarrollando un programa para gestionar las calificaciones de un estudiante. Debes seguir estos pasos:

- Crea una lista llamada notas con al menos 5 calificaciones (números del 0 al 10).
- Agrega una nueva calificación al final de la lista con append().
- Elimina la calificación más baja usando remove() o pop().
- Calcula el promedio de las calificaciones y muéstralo en pantalla.
- Ordena las calificaciones de mayor a menor usando sort(reverse=True).
- Muestra la lista de notas actualizada.
'''
#Crea una lista llamada notas con al menos 5 calificaciones (números del 0 al 10).
Notas_11 = [8, 1, 6, 9, 5]
print(Notas_11) # Salida: [8, 1, 6, 9, 5]

#Agrega una nueva calificación al final de la lista con append()
Notas_11.append(10)
print(Notas_11)# Salida: [8, 1, 6, 9, 5, 10]

#Elimina la calificación más baja usando remove() o pop().
Notas_11.remove(1) #la mas baja
print(Notas_11)#Salida: [8, 6, 9, 5, 10]
Notas_11.pop(4) # elimina la nota mas alta
print(Notas_11)# Salida[8, 6, 9, 5]

#Calcula el promedio de las calificaciones y muéstralo en pantalla.
Promedio = sum(Notas_11)/len(Notas_11)
print(f"{Promedio} Es el promedio de la calificaciones" ) #Respuesta o salida: 7


#Ordena las calificaciones de mayor a menor usando sort(reverse=True).
Notas_11.sort(reverse=True)
print(Notas_11)#Salida: [9, 8, 6, 5]

#Muestra la lista de notas actualizada.
print(Notas_11)# Salida: [9, 8, 6, 5]
