def calcular_promedio(notas):
    return sum(notas) / len(notas)


def main():
    notas = []
    cantidad = int(input("¿Cuántas notas quiere ingresar? "))

    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    print(f"El promedio es: {promedio:.2f}")

    if promedio >= 70:
        print("Aprobó el curso")
    else:
        print("No aprobó el curso")


main()
