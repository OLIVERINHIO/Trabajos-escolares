comentario= " Me encantó este producto y es increible, además increiblemente útil y aparte lo recomiendo mucho y deja el cabello muy suave"
#eliminar espacios en blanco al inicioy al final
comentario=comentario.strip()
print(comentario)
#reemplazar la palabra "increiblemente" por "muy"
print(comentario.replace("increiblemente","muy"))
#contar cuantas veces aparece la palabra "y"
palabras=comentario.split()
conteo_y=palabras.count("y")
print(f"Veces que aparece 'y':{conteo_y}")
#dividir la reseña en una lista de palabras
frase="Python es divertido"
lista_palabras=frase.split()
nueva_frase="-".join(lista_palabras)
print(nueva_frase,frase,lista_palabras)
#determinar cuantas palabras tiene el comentario
palabras=comentario.split()
conteo_palabras=len(palabras)
print(f"Numero total de palabras: {conteo_palabras}")
