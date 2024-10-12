import random

caracters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456lo"
longitud = int(input("ingresa la longitud de tu contraseña:"))
resultado = ""

for i in range(longitud):
    resultado += random.choice(caracters)

print(f"tu contraseña con una longitud de {longitud} es: {resultado}")
