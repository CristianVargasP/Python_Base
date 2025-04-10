# Introduccion

## Python
En este documento exploraremos dos pilares fundamentales para construir una buena base: los bucles y las estructuras de datos. Entender cómo funcionan los bucles (como `for` y `while`) nos permite automatizar tareas, mientras que dominar las estructuras de datos (listas, tuplas, diccionarios y conjuntos)nos da las herramientas para organizar y trabajar eficientemente con la información. Aprender estos conceptos es esencial para avanzar con seguridad en el camino del programador.

### Bucles 
Secuencia de instrucciones que se repiten hasta que se cumple una condición.
Los cuales tenemos el FOR y el WHILE que se veran a continuacion: 

- ### FOR
  Se utiliza para repetir una accion un numero determinado de veces, recorriendo elementos de una lista, rango, cadena, diccionario, etc

  Estructura:
  
   **for** variable **in** iterable:
  - **VARIABLE:** Nombre que le das a cada elemento del iterable mientras se recorre
  - **INTERABLE:** Cualquier objeto que se puede recorrer elemento por elemento
       Ejemplos de interables:
    - Listas
    - Tuplas
    - Cadenas de texto
    - Diccionarios
    - Conjuntos
    - Objetos de tipo 


    
- ### WHILE
  El bucle while repite un bloque de codgio mientras una condicion sea verdadera. Se usa cuando no sabes cuantas veces necesitas repetir algo.

  **“Sigue haciendo esto una y otra vez, mientras algo sea verdad.”**
  
  Es como cuando tu mamá te dice:
  “Sigue limpiando tu cuarto mientras esté desordenado.”
  → Cuando ya está ordenado (la condición ya no es verdad), paras.

  Estructura:
  
  **while** condición:

  bloque de código
  - La **condicion** se evalua antes de cada iteracion
  - El **bloque de codigo** se ejecuta solo si la condicion es **True**


### Estructura de datos 
Es una froma de organizar y guardar informacion para poder usarla mas facilmente en tus progrmas.

**Las principales estructuras de datos en Python:**
- Listas(List)

  Permire guardar una coleccion de elementos en un orden especifico
  
  - Se puede relacionar como una fila de cajas, donde cada caja tiene algo adentro y un numero que indica su posicion(indice)
    
    Explicacion para niños:
    - Una lista es como una mochila con muchos bolsillos, donde puedes guardar lo que quieras y sacar lo que necesites cuando quieras.
      
    **Caracteristicas**
    - Puede guardar cualquier tipo de dato: Numero, texto, otras listas, etc.
    - Es mutable
    - Cada elemento tiene una posicion, comenzando desde el 0
    - Se puede recorrer con bucles
      
- Tuplas(tuple)

  Coleccion ordenada de elementos, igual que una Lista, pero no se puede modificar una vez creada.

  Explicación para un niño:
  
Una tupla es como una foto impresa: puedes verla, contar cuántas personas hay, pero no puedes cambiarla después de tomarla.

  **Caracteristicas:**
  - Tiene un orden
  - No se puede cambiar, agregar ni eliminar elementos despues de crearse
  - Son mas rapidos que las Listas
  - Se usan para guardar datos fijos o que no deben cambiar

- Diccionarios(dict)

  Permite guardar informacion dondo cada elemento tiene una **clave(key)** y un **valor(value)**

  Explicación para un niño:
  
Un diccionario es como una mochila con etiquetas.
En vez de decir "dame el bolsillo 1", dices "dame lo que tiene la etiqueta 'edad'", y él te lo da.


  **Caracteristicas:**
  - Cada dato esta guardado como **clave:valor**
  - las claves deben ser unicas(No se puede repetir)
  - Los valores pueden ser de cualquier tipo
  - Son ideales para buscar datos rapidos

    Cuandp usarlo:
    - Cuando quieras relacionar datos
    - Cunado necesitas buscar algo rapido sin preocuparte por el orden

  
- Conjuntos(set)
  Guarda elementos unicos(sin repetir) y sin un orden especifico

  Explicación para un niño:
  
Un conjunto es como una caja de juguetes donde no puedes tener dos iguales.
Si metes otro igual, solo se queda uno.


**Caracteristicas**
- No permites elementos repetidos
- No tiene un orden definido(No puedes acceder por indice)
- Muy util para hacer operaciones como:
  - union
  - interseccion
  - Diferencia
    
**¿Cuándo usar un conjunto?**
- Para eliminar duplicados de una lista
- para comparar grupos de elementos
- Cuando no importe el orden

  







  



  

