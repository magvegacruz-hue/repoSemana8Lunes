#Leer un archivo "misDatos.txt usando with)"
with open('misDatos.txt', 'r', encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)