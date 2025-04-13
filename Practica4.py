#Programa 1 funciones de cadenas
texto = "Python"
print(texto[0])
print(texto[-1])
print(texto[1:4])
#programa 2
texto2 = "Hola Mundo"
print(len(texto2))
print(texto2.strip())
print(texto2.replace("Hola","Adios"))
#Programa 3
frase="Python es divertido"
lista_palabras=frase.split()
nueva_frase="-".join(lista_palabras)
print(nueva_frase,frase,lista_palabras)
#programa 4
texto3="Aprender Python es genial"
print("Python"in texto3)
print(texto3.find("Python"))
print(texto3.count("e"))
#programa 5
nombre="Oliver"
edad=20
print(f"Mi nombre es {nombre} y tengo {edad} años. ")
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))
#programa 6
print("12345".isdigit())
print("Hola".isalpha())
print("Pothon123".isalnum())
print("python".islower())
print("PYTHON".isupper())
#programa 7
texto="Python es un lenguaje de prigramascion increible. Aprender python es muy útil. "
palabras=texto.split()
conteo_palabras=len(palabras)
conteo_python=texto.lower().count("python")
print(f"Numero total de palabras: {conteo_palabras}")
print(f"Veces que aparece 'python':{conteo_python}")