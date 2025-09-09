# 1.ograma para imprimir los números primos menores o iguales a un número dado

# Pedir al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if n <= 0:
    print("Debe ingresar un número entero positivo.")
else:
    contador_primos = 0  # Para contar los primos encontrados

    print(f"Números primos menores o iguales a {n}:")
    
    # Recorremos todos los números desde 2 hasta n
    for num in range(2, n + 1):
        es_primo = True  # Suponemos que es primo

        # Verificamos divisibilidad desde 2 hasta num-1
        for divisor in range(2, num):
            if num % divisor == 0:
                es_primo = False
                break  # Si no es primo, salimos del ciclo
        

        # Si sigue siendo primo después de la verificación
        if es_primo:
            print(num, end=" ")
            contador_primos += 1

    # Salto de línea
    print("\nCantidad de primos encontrados:", contador_primos)


 #2Definición de la función con parámetro por omisión
def calcular_descuento(precio, descuento=10):
    # Se aplica el descuento
    precio_final = precio - (precio * descuento / 100)
    return precio_final


# Programa principal
total_pagar = 0
cantidad_productos = 3  # Se piden al menos 3 precios, pero puede ampliarse

for i in range(1, cantidad_productos + 1):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    # Aplicar descuento usando la función
    precio_con_descuento = calcular_descuento(precio)
    print(f"Precio final con descuento del 10%: {precio_con_descuento}")
    total_pagar += precio_con_descuento

# Mostrar el total a pagar
print("\nEl valor total a pagar por los 3 productos es:", total_pagar)

#3.
def analizar_texto(*args, **kwargs):
    # Unimos todos los textos recibidos en *args
    texto = " ".join(args).lower()
    
    # Inicializamos contadores
    total_vocales = 0
    total_palabras = 0

    # Si el usuario pide contar vocales
    if kwargs.get("contar_vocales", False):
        for letra in texto:
            if letra in "aeiou":
                total_vocales += 1
        print("Cantidad total de vocales:", total_vocales)

    # Si el usuario pide contar palabras
    if kwargs.get("contar_palabras", False):
        total_palabras = len(texto.split())
        print("Cantidad total de palabras:", total_palabras)


# -------------------------------
# Programa principal
# Pedir al usuario cuántos textos quiere ingresar
n = int(input("¿Cuántas frases o palabras desea ingresar? "))

textos = []
for i in range(1, n + 1):
    frase = input(f"Ingrese el texto {i}: ")
    textos.append(frase)

# Preguntar qué desea analizar
opcion_vocales = input("¿Desea contar vocales? (s/n): ").lower() == "s"
opcion_palabras = input("¿Desea contar palabras? (s/n): ").lower() == "s"

# Llamar la función con los textos y las opciones
analizar_texto(*textos, contar_vocales=opcion_vocales, contar_palabras=opcion_palabras)


#4Programa para dividir dos números enteros con manejo de errores

try:
    # 1. Pedir al usuario dos números enteros
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    # 2. Calcular la división
    resultado = num1 / num2

except ValueError:
    # 3. Si el usuario ingresa un valor no numérico
    print("Error: Debe ingresar números enteros.")

except ZeroDivisionError:
    # 4. Si intenta dividir entre cero
    print("Error: No se puede dividir entre cero.")

else:
    # Si no hubo errores, mostrar el resultado
    print(f"El resultado de {num1} / {num2} es: {resultado}")


#5.-- Funciones de gestión de estudiantes ---

def promedio_notas(estudiantes):
    """Calcula el promedio de las notas"""
    if len(estudiantes) == 0:
        return 0
    suma = 0
    for est in estudiantes:
        suma += est["nota"]
    return suma / len(estudiantes)


def mejor_estudiante(estudiantes):
    """Retorna el nombre y nota del mejor estudiante"""
    if len(estudiantes) == 0:
        return None
    mejor = estudiantes[0]
    for est in estudiantes:
        if est["nota"] > mejor["nota"]:
            mejor = est
    return mejor


def peor_estudiante(estudiantes):
    """Retorna el nombre y nota del peor estudiante"""
    if len(estudiantes) == 0:
        return None
    peor = estudiantes[0]
    for est in estudiantes:
        if est["nota"] < peor["nota"]:
            peor = est
    return peor


# --- Programa principal ---

estudiantes = []

print("=== Sistema de Gestión de Estudiantes ===")
print("Escriba 'fin' como nombre para terminar.\n")

# 1. Ingreso de estudiantes usando ciclo while
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        if nota < 0 or nota > 5:
            print("La nota debe estar entre 0 y 5. Intente de nuevo.")
            continue
        estudiantes.append({"nombre": nombre, "nota": nota})
    except ValueError:
        print("Error: La nota debe ser un número. Intente de nuevo.")

# 4. Reporte final
print("\n=== REPORTE FINAL ===")
print("Número de estudiantes registrados:", len(estudiantes))

if len(estudiantes) > 0:
    prom = promedio_notas(estudiantes)
    mejor = mejor_estudiante(estudiantes)
    peor = peor_estudiante(estudiantes)

    print(f"Promedio de notas: {prom:.2f}")
    print(f"Mejor estudiante: {mejor['nombre']} con nota {mejor['nota']}")
    print(f"Peor estudiante: {peor['nombre']} con nota {peor['nota']}")

    # Ordenar estudiantes de menor a mayor nota (sin usar librerías externas)
    for i in range(len(estudiantes)):
        for j in range(i + 1, len(estudiantes)):
            if estudiantes[i]["nota"] > estudiantes[j]["nota"]:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]

    print("\nEstudiantes ordenados por nota (menor a mayor):")
    for est in estudiantes:
        print(f"{est['nombre']} - {est['nota']}")
else:
    print("No se ingresaron estudiantes.")












