print("""PRACTICA 2
Uso de Variables, impresion de mensajes,
mayusculas y minusculas
Oliver Absalon Estrada Lozano-""")

nombre = input("Ingresa tu nombre: ")
print(f"Nombre ingresado correctamente: {nombre.upper()}")

semestre = input("Ingresa tu semestre: ")
print(f"semestre ingresado correctamente: {semestre}")

matricula = input("Ingresa tu matricula: ")
print(f"matricula ingresado correctamente: {matricula}")

licenciatura = input("Ingresa tu licenciatura: ")
print(f"licenciatura ingresado correctamente: {licenciatura}")

genero = input("Ingresa tu genero: ")
print(f"genero ingresado correctamente: {genero}")

print("\nGracias por llenar los datos del formulario, los datos que ingresaste son:")
print(f"Nombre: {nombre}\t\tsemestre: {semestre}")
print(f"matricula: {matricula}\t\tlicenciatura: {licenciatura}")
print(f"genero electrónico: {genero}")