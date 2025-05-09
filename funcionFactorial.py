
def factorial(x):
    if x < 0:
        return 0
    total = 1
    while x > 1:
        total *= x
        x -= 1
    return total

seguir = True
real = True #esta variable solo es para quienes quieran afrontar la realidad

while seguir:
    numero = int(input("Inserte un numero para calcular su factorial o escriba [-777] para terminar: "))
    if numero != -777:
        print(f"{numero}! es igual a {factorial(numero)}")
    else:
        seguir = False

print("Programa finalizado exitosamente")