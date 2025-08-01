def evaluar_numero(numero):
    if numero == 10:
        print("El número ingresado es 10")
    elif numero == 7:
        print("Se ha ingresado un comodín")
    elif numero % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

# Función principal
def main():
    print("=== Evaluador de Números ===")
    print("Ingresa -1 para salir.\n")
    
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            if numero == -1:
                print("Programa finalizado.")
                break
            evaluar_numero(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Invocar la función principal
if __name__ == "__main__":
    main()