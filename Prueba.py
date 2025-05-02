def printCategory(age):
    if age > 18:
        print('Adulto')
    elif age > 65:
        print('Adulto mayor')
    else:
        print('Niño')

# Solicita la edad al usuario
try:
    edad = int(input("Por favor, ingresa tu edad: "))
    printCategory(edad)
except ValueError:
    print("Por favor, ingresa un número válido.")