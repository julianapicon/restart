def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(codigo)
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

# Pedir frase y desplazamiento al usuario
frase = input("Introduce la frase a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento (número entero): "))

# Cifrado
cifrado = cifrar_cesar(frase, desplazamiento)
print("Frase cifrada:", cifrado)

# Descifrado
descifrado = descifrar_cesar(cifrado, desplazamiento)
print("Frase descifrada:", descifrado)
