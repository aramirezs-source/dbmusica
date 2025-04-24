import math

def menu():
    print('\n1) Suma números')
    print('2) Resta números')
    print('3) Multiplica números')
    print('4) Divideix números')
    print('5) Potència (x^y)')
    print('6) Mòdul (resta de la divisió)')
    print('7) Arrel quadrada')
    print('0) Sortir del programa')
    
    try:
        op = int(input("Tria opció: "))
    except ValueError:
        print("Error: Has d'introduir un número enter.")
        return menu()
    
    return op

def introduir_numero(missatge="Introdueix un número: "):
    while True:
        try:
            return float(input(missatge))
        except ValueError:
            print("Error: No has introduït un número vàlid.")

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divideix(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: No es pot dividir per zero."

def potencia(x, y):
    return x ** y

def modul(x, y):
    return x % y

def arrel_quadrada(x):
    try:
        if x < 0:
            raise ValueError("No es pot calcular l'arrel quadrada d'un número negatiu.")
        result = math.sqrt(x)
    except ValueError as e:
        return f"Error: {e}"
    else:
        return result
    finally:
        print("Operació d'arrel quadrada finalitzada.")

# Programa principal
opcio = menu()
while opcio != 0:
    if opcio in [1, 2, 3, 4, 5, 6]:
        a = introduir_numero("Introdueix el primer número: ")
        b = introduir_numero("Introdueix el segon número: ")
    elif opcio == 7:
        a = introduir_numero("Introdueix un número per calcular l'arrel quadrada: ")
    
    if opcio == 1:
        print("Resultat:", suma(a, b))
    elif opcio == 2:
        print("Resultat:", resta(a, b))
    elif opcio == 3:
        print("Resultat:", multiplica(a, b))
    elif opcio == 4:
        print("Resultat:", divideix(a, b))
    elif opcio == 5:
        print("Resultat:", potencia(a, b))
    elif opcio == 6:
        print("Resultat:", modul(a, b))
    elif opcio == 7:
        print("Resultat:", arrel_quadrada(a))
    else:
        print("T'has equivocat d'opció")
    
    opcio = menu()

print("Fins la pròxima!")