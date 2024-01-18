"""Hacer un programa que gestiones datos para una escuela. 
El programa tiene que ser capaz de: 
 
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
notas, cantidad de faltas, cantidad de amonestaciones recibidas. 
 
Recomendación: Para llevar un registro de estos dato se puede 
utilizar un diccionario estructurado de la siguiente manera: 
{ 
“Alumnos” : [alumno1,alumno2,alumno3 ] 
} 
Donde cada alumno es otro diccionario estructurado de la  
 
siguiente forma: 
{ 
 “Nombre”: nombre de alumno, 
“Apellido” : apellido de alumno, 
“DNI” : DNI de alumno 
“Fecha de nacimiento”, fecha de nacimiento de alumno, 
“Tutor” : nombre y apellido de tutor, 
“Notas” : todas las notas del alumno, 
“Faltas” : cantidad de faltas, 
“amonestaciones” : cantidad de amonestaciones 
 
} 
 
En esta estructura: 
Datos  = { 
“Alumnos” : [alumno1,alumno2,alumno3 ] 
} 
Para acceder por ejemplo al numero de DNI del tercer alumno 
podríamos hacer algo así: 
 Datos[“Alumnos”][2][“DNI”] 
 
Este es un ejemplo de estructura, se puede cambiar 
completamente o hacer algunos cambios sobre el para mejorar el 
orden (si lo consideran necesario) 
 
 
b) Mostrar los datos de cada alumno 
c) Modificar los datos de los alumnos 
d) Agregar alumnos 
e) Expulsar alumnos 
 """


def muestra_alu(alu):
    print(f"Datos del alumno:")
    print(f"Nombre: {alu['Nombre']}")
    print(f"Apellido: {alu['Apellido']}")
    print(f"DNI: {alu['DNI']}")
    print(f"Fecha de nacimiento: {alu['Fecha de nacimiento']}")
    print(f"Tutor: {alu['Tutor']}")
    print(f"Notas: {alu['Notas']}")
    print(f"Faltas: {alu['Faltas']}")
    print(f"Amonestaciones: {alu['Amonestaciones']}")

def all_alu(alumnos):
    for i in range(len(alumnos)):
        print(f"Datos del alumno {i + 1}:")
        print(f"Nombre: {alumnos[i]['Nombre']}")
        print(f"Apellido: {alumnos[i]['Apellido']}")
        print(f"DNI: {alumnos[i]['DNI']}")
        print(f"Fecha de nacimiento: {alumnos[i]['Fecha de nacimiento']}")
        print(f"Tutor: {alumnos[i]['Tutor']}")
        print(f"Notas: {alumnos[i]['Notas']}")
        print(f"Faltas: {alumnos[i]['Faltas']}")
        print(f"Amonestaciones: {alumnos[i]['Amonestaciones']}")

def modificar_datos_alumno(alumnos, indice_alumno, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento,
                           nuevo_tutor, nuevas_notas, nuevas_faltas, nuevas_amonestaciones):
    alumno = alumnos[indice_alumno]
    alumno["Nombre"] = nuevo_nombre
    alumno["Apellido"] = nuevo_apellido
    alumno["Fecha de nacimiento"] = nueva_fecha_nacimiento
    alumno["Tutor"] = nuevo_tutor
    alumno["Notas"] = nuevas_notas
    alumno["Faltas"] = nuevas_faltas
    alumno["Amonestaciones"] = nuevas_amonestaciones

def agregar_alumno(alumnos, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones):
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    alumnos.append(nuevo_alumno)

def expulsar_alumno(alumnos, indice_alumno):
    if 0 <= indice_alumno < len(alumnos):
        alumno_expulsado = alumnos.pop(indice_alumno)
        print(f"Se ha expulsado al alumno {alumno_expulsado['Nombre']} {alumno_expulsado['Apellido']}.")
    else:
        print("no se encontro el indice")



def cuerpo():
    alumnos = []

    while True:
        print("Menú:")
        print("a Mostrar datos de un alumno")
        print("b Mostrar datos de todos los alumnos")
        print("c Modificar datos de un alumno")
        print("d Agregar un nuevo alumno")
        print("e Expulsar un alumno")
        print("sali: Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            indice = int(input("Ingrese el índice del alumno (empezando desde 1): ")) - 1
            muestra_alu(alumnos[indice])
        elif opcion == "b":
            all_alu(alumnos)
        elif opcion == "c":
            indice = int(input("Ingrese el índice del alumno a modificar (empezando desde 1): ")) - 1
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento: ")
            nuevo_tutor = input("Ingrese el nuevo tutor: ")
            nuevas_notas = input("Ingrese las nuevas notas (separadas por comas): ").split(",")
            nuevas_faltas = int(input("Ingrese la nueva cantidad de faltas: "))
            nuevas_amonestaciones = int(input("Ingrese la nueva cantidad de amonestaciones: "))
            modificar_datos_alumno(alumnos, indice, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento,
                                   nuevo_tutor, nuevas_notas, nuevas_faltas, nuevas_amonestaciones)
        elif opcion == "d":
            nombre = input("Ingrese el nombre del nuevo alumno: ")
            apellido = input("Ingrese el apellido del nuevo alumno: ")
            dni = input("Ingrese el DNI del nuevo alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo alumno: ")
            tutor = input("Ingrese el nombre y apellido del tutor del nuevo alumno: ")
            notas = input("Ingrese las notas del nuevo alumno (separadas por comas): ")
            faltas = int(input("Ingrese la cantidad de faltas del nuevo alumno: "))
            amonestaciones = int(input("Ingrese la cantidad de amonestaciones del nuevo alumno: "))
            agregar_alumno(alumnos, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones)
        elif opcion == "e":
            indice = int(input("Ingrese el índice del alumno a expulsar (empezando desde 1): ")) - 1
            expulsar_alumno(alumnos, indice)
        elif opcion == "sali":
            print("Programa finalizado")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


cuerpo()

