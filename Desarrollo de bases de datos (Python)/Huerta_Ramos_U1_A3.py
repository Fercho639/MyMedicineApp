#Crea un programa que permita realizar operaciones matemáticas básicas 
# (suma, resta, multiplicación, división) y aplicar funciones matemáticas 
# predefinidas (como raíz cuadrada, exponenciales y/o logaritmos).
 
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))

    else:
        print("Opción no válida. Por favor, intente de nuevo.")




 
