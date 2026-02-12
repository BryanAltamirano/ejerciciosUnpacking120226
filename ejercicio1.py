# arreglo de estudiantes con nombre y calificaciones
estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]
#aqui se hizo el unpacking para obtener el nombre y las calificaciones de cada estudiante
def calcular_Promedio(*calificaciones):
    # aqui se hace el unpacking para calcular el promedio, máximo y mínimo de las calificaciones
    promedio = sum(calificaciones) / len(calificaciones)
    # retornamos el promedio, el máximo y el mínimo como una tupla
    return promedio, max(calificaciones), min(calificaciones)

# creamos el diccionario de resultados con unpacking
def mostrar_resultados(**datos):
    #imprimimos los resultados con unpacking
    print(f"\nResultados finales:\n")
    # usamos el for para acceder a cada estudiante y su información
    for nombre, info in datos.items():
        print(f"Estudiante: {nombre} :", *info.items())

# guardamos los resultados en un diccionario usando unpacking
resultados = {}
# iteramos sobre los estudiantes y calculamos su promedio, máximo y mínimo usando unpacking
for estudiante in estudiantes:
    nombre, *calificaciones = estudiante
    promedio, maximo, minimo = calcular_Promedio(*calificaciones)
    # guardamos los resultados en el diccionario usando unpacking
    resultados[nombre] = {
        "promedio": promedio,
        "max": maximo,
        "min": minimo
    }
# mostramos los resultados usando unpacking
mostrar_resultados(**resultados)

# obtenemos el estudiante con el mayor promedio usando unpacking
mejor_nombre, mejor_info = max(resultados.items(), key=lambda x: x[1]["promedio"])
# imprimimos el estudiante con el mayor promedio usando unpacking
print(f"\nMayor promedio: {mejor_nombre} con {mejor_info['promedio']}")
