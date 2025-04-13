#punto 1
nombre=(input("Ingresa su nombre"))
edad=(input("Ingresa su edad"))
ciudad=(input("Ingresa su ciudad"))
pasatiempo=(input("Ingresa su pasatiempo"))
#punto 2
print(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo} ")
#punto 3
print(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo} ".upper())
print(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo} ".lower())
#punto 4
texto=(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo} ")
palabras=texto.split()
conteo_palabras=len(palabras)
print(f"Numero total de palabras: {conteo_palabras}")
#punto 5
print(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo.replace(pasatiempo,"descubrir cosas nuevas")} ")
#punto 6
frase=(f"{nombre} tiene {edad} años vive en {ciudad} y le gusta {pasatiempo} ")
lista_palabras=frase.split()
nueva_frase="-".join(lista_palabras)
print(nueva_frase*4)