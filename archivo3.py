#Leer los nombres, apellidos, edad y carrera de un estudiante
#guardo en un archivo llamado estudiante.txt

nombres = input("Dime tus nombres: ")
apellidos = input("Ahora tus apellidos: ")
edad = int(input("Dime tu edad: "))
carrera = input("Ahora tu carrera: ")

datos = f"Nombre: {nombres.title()}\nApellidos: {apellidos.title()} \nEdad: {edad}\nCarrera: {carrera.title()}\n"
with open("estudiante.txt", 'a', encoding="utf-8") as archivo:
    archivo.write(datos)
print("Archivo creado satisfactoriamente")
