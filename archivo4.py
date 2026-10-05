#crea un programa que permita guardar n cantidad de notas en un archivo, leer las nota, calcular el promedio
#la nota mas alta y la mas baja
notas = []
def pedirNotas():
    while True:
        try:
            nota = int(input("Dime la nota: "))
            return nota
        except ValueError:
            print("Debe ser un valor numerico")
        
def agregarNota():
    while True:
        nota = pedirNotas()
        if nota > 0 and nota <= 100:
            notas.append(nota)
        resp = input("Otra nota [S|N]: ")
        if resp.lower() == 'n':
            return
        
def guardarNota():
    with open("notas.txt", "a+") as notasFile:
        for nota in notas:
            notasFile.write(str(nota) + "\n")
    print("Registro guardado.")

def calcularPromedio():
    suma = 0
    for nota in notas:
        suma += nota
    return suma/len(notas)

def calcularMayor():
    mayor = notas[0]
    for nota in notas:
        if nota > mayor:
            mayor = nota
    return mayor

def calcularMenor():
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor


agregarNota()
guardarNota()
print(f"Promedio: {calcularPromedio()}")
print(f"Mayor nota: {calcularMayor()}")
print(f"Menor nota: {calcularMenor()}")