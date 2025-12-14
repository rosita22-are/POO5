
# PROGRAMA TRADICIONAL: PROMEDIO SEMANAL


def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de la semana (7 días):\n")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temps):
    return sum(temps) / len(temps)

def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal es: {promedio:.2f}°C")


main()
