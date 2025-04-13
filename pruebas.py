texto="Python es un lenguaje de prigramascion increible. Aprender python es muy útil. "
palabras=texto.split()
conteo_palabras=len(palabras)
conteo_python=texto.lower().count("python")
print(f"Numero total de palabras: {conteo_palabras}")
print(f"Veces que aparece 'python':{conteo_python}")